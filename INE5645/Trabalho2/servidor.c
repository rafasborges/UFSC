#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <fcntl.h>
#include <pthread.h>
#include <semaphore.h>
#include <time.h>

#define DEFAULT_PORT 8080
#define DEFAULT_BUFFER_SIZE 128
#define DEFAULT_MAX_CLIENTS 5
#define THROTTLE_RATE 256 

sem_t sem_conexoes;
pthread_mutex_t client_lock; 
int active_clients = 0;      

typedef struct {
    int port;
    int max_clients;
    size_t buffer_size;
} server_config_t;


void parse_arguments(int argc, char *argv[], server_config_t *config) {
    for (int i = 1; i < argc; i++) {
        if (strcmp(argv[i], "--port") == 0 && i + 1 < argc) {
            config->port = atoi(argv[++i]);
        } else if (strcmp(argv[i], "--max_clients") == 0 && i + 1 < argc) {
            config->max_clients = atoi(argv[++i]);
        } else if (strcmp(argv[i], "--buffer_size") == 0 && i + 1 < argc) {
            config->buffer_size = atoi(argv[++i]);
        } else {
            fprintf(stderr, "Argumento desconhecido: %s\n", argv[i]);
            exit(EXIT_FAILURE);
        }
    }
}

void throttle_transfer(size_t bytes_transferred) {
    static clock_t last_time = 0;
    clock_t current_time = clock();

    double elapsed = (double)(current_time - last_time) / CLOCKS_PER_SEC;
    double expected_time = (double)bytes_transferred / THROTTLE_RATE;

    if (elapsed < expected_time) {
        usleep((useconds_t)((expected_time - elapsed) * 1000000));
    }

    last_time = current_time;
}

void *handle_client(void *arg) {
    int client_sock = *(int *)arg;
    free(arg); 
    char dest_path[256];
    char partial_path[256];
    FILE *file;
    ssize_t bytes_received, total_bytes = 0;
    int end_received = 0;
    char buffer[DEFAULT_BUFFER_SIZE + 1]; 
    char temp_buffer[DEFAULT_BUFFER_SIZE + 1]; 

    pthread_mutex_lock(&client_lock);
    int current_buffer_size = DEFAULT_BUFFER_SIZE / active_clients; 
    pthread_mutex_unlock(&client_lock);

    if (recv(client_sock, dest_path, sizeof(dest_path), 0) <= 0) {
        perror("Erro ao receber o caminho do arquivo de destino");
        close(client_sock);
        sem_post(&sem_conexoes); 
        pthread_exit(NULL);
    }

    if (snprintf(partial_path, sizeof(partial_path), "%s.part", dest_path) >= sizeof(partial_path)) {
        fprintf(stderr, "Caminho do arquivo muito longo\n");
        close(client_sock);
        sem_post(&sem_conexoes); 
        pthread_exit(NULL);
    }

    if (access(partial_path, F_OK) == 0) {
        file = fopen(partial_path, "ab");
        if (!file) {
            perror("Erro ao abrir o arquivo parcial existente");
            close(client_sock);
            sem_post(&sem_conexoes); 
            pthread_exit(NULL);
        }
        fseek(file, 0, SEEK_END); 
        total_bytes = ftell(file); 
        printf("Arquivo parcial encontrado.");
    } else {
        file = fopen(partial_path, "wb");
        if (!file) {
            perror("Erro ao criar o arquivo parcial");
            close(client_sock);
            sem_post(&sem_conexoes);
            pthread_exit(NULL);
        }
        printf("Arquivo parcial não encontrado, iniciando um novo arquivo.\n");
    }

    printf("Cliente [%d]: Iniciando transferência de arquivo.\n", client_sock);


    while ((bytes_received = recv(client_sock, buffer, DEFAULT_BUFFER_SIZE, 0)) > 0) {
        buffer[bytes_received] = '\0'; 
        char *end_position = strstr(buffer, "END"); 

        if (end_position != NULL) {
            size_t data_size = end_position - buffer;
            if (data_size > 0) {
                fwrite(buffer, 1, data_size, file);
                total_bytes += data_size;
            }
            end_received = 1;
            printf("Recebeu 'END', total de %zu bytes transferidos.\n", total_bytes);
            break; 
        } else {
            fwrite(buffer, 1, bytes_received, file);
            total_bytes += bytes_received;
        }

        printf("Cliente [%d]: Bytes transferidos até agora: %zu bytes\n", client_sock, total_bytes);

        throttle_transfer(bytes_received);
    }

    if (bytes_received == 0 && !end_received) {
        printf("Cliente encerrou a conexão sem enviar 'END'.\n");
    } else if (bytes_received < 0) {
        perror("Erro ao receber dados");
    } else if (end_received && rename(partial_path, dest_path) != 0) {
        perror("Erro ao renomear o arquivo parcial");
    } else if (end_received) {
        printf("Transferência concluída: %s\n", dest_path);
    }

    fclose(file);
    close(client_sock);

    pthread_mutex_lock(&client_lock);
    active_clients--;
    pthread_mutex_unlock(&client_lock);
    sem_post(&sem_conexoes); 
    pthread_exit(NULL);
}

int main(int argc, char *argv[]) {
    server_config_t config = {DEFAULT_PORT, DEFAULT_MAX_CLIENTS, DEFAULT_BUFFER_SIZE};
    int server_sock, client_sock;
    struct sockaddr_in server_addr, client_addr;
    socklen_t addr_len = sizeof(client_addr);
    pthread_t tid;

    parse_arguments(argc, argv, &config);
    sem_init(&sem_conexoes, 0, config.max_clients);
    pthread_mutex_init(&client_lock, NULL);

    server_sock = socket(AF_INET, SOCK_STREAM, 0);
    if (server_sock < 0) {
        perror("Erro ao criar o socket");
        exit(EXIT_FAILURE);
    }

    server_addr.sin_family = AF_INET;
    server_addr.sin_port = htons(config.port);
    server_addr.sin_addr.s_addr = INADDR_ANY;

    if (bind(server_sock, (struct sockaddr *)&server_addr, sizeof(server_addr)) < 0) {
        perror("Erro ao associar o socket");
        close(server_sock);
        exit(EXIT_FAILURE);
    }

    if (listen(server_sock, config.max_clients) < 0) {
        perror("Erro ao escutar por conexões");
        close(server_sock);
        exit(EXIT_FAILURE);
    }

    printf("Servidor iniciado na porta %d (Max clientes: %d, Buffer: %zu bytes)\n",
           config.port, config.max_clients, config.buffer_size);

    while ((client_sock = accept(server_sock, (struct sockaddr *)&client_addr, &addr_len)) >= 0) {
        if (sem_trywait(&sem_conexoes) != 0) {
            char *message = "Servidor ocupado. Tentando novamente...\n";
            send(client_sock, message, strlen(message), 0);

            sem_wait(&sem_conexoes);
        }

        pthread_mutex_lock(&client_lock);
        active_clients++;
        pthread_mutex_unlock(&client_lock);

        int *pclient = malloc(sizeof(int));
        *pclient = client_sock;

        if (pthread_create(&tid, NULL, handle_client, pclient) != 0) {
            perror("Erro ao criar a thread para cliente");
            close(client_sock);
            free(pclient);

            sem_post(&sem_conexoes);

            pthread_mutex_lock(&client_lock);
            active_clients--;
            pthread_mutex_unlock(&client_lock);
        } else {
            pthread_detach(tid); 
        }
    }

    close(server_sock);
    sem_destroy(&sem_conexoes);
    pthread_mutex_destroy(&client_lock);
    return 0;
}
