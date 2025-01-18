#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <fcntl.h>
#include <errno.h>

#define BUFFER_SIZE 128
#define RETRY_LIMIT 5      
#define RETRY_INTERVAL 2 

void send_file(const char *filename, const char *server_ip, int server_port, const char *dest_path) {
    int sockfd;
    struct sockaddr_in server_addr;
    char buffer[BUFFER_SIZE];
    FILE *file;
    char part_file[256];
    size_t bytes_read, bytes_sent, offset = 0;
    int attempt = 0;

    snprintf(part_file, sizeof(part_file), "%s.part", filename);

    if (access(part_file, F_OK) == 0) {
        FILE *part = fopen(part_file, "rb");
        fseek(part, 0, SEEK_END);
        offset = ftell(part);
        fclose(part);
        printf("Retomando transferência a partir de %zu bytes.\n", offset);
    }

    file = fopen(filename, "rb");
    if (!file) {
        perror("Erro ao abrir o arquivo");
        exit(EXIT_FAILURE);
    }

    fseek(file, offset, SEEK_SET);

    server_addr.sin_family = AF_INET;
    server_addr.sin_port = htons(server_port);
    inet_pton(AF_INET, server_ip, &server_addr.sin_addr);

    while (attempt < RETRY_LIMIT) {
        sockfd = socket(AF_INET, SOCK_STREAM, 0);
        if (sockfd < 0) {
            perror("Erro ao criar socket");
            fclose(file);
            exit(EXIT_FAILURE);
        }

        if (connect(sockfd, (struct sockaddr *)&server_addr, sizeof(server_addr)) == 0) {
            printf("Conexão estabelecida com o servidor na tentativa %d!\n", attempt + 1);
            break; 
        } else {
            printf("Tentativa %d: Não foi possível conectar ao servidor. Erro: %s\n", attempt + 1, strerror(errno));
            close(sockfd);
            attempt++;
            if (attempt < RETRY_LIMIT) {
                printf("Tentando novamente em %d segundos...\n", RETRY_INTERVAL);
                sleep(RETRY_INTERVAL);
            }
        }
    }

    if (attempt == RETRY_LIMIT) {
        printf("Não foi possível conectar ao servidor após %d tentativas. Encerrando.\n", RETRY_LIMIT);
        fclose(file);
        exit(EXIT_FAILURE);
    }

    send(sockfd, dest_path, strlen(dest_path) + 1, 0);

    while ((bytes_read = fread(buffer, 1, BUFFER_SIZE, file)) > 0) {
        bytes_sent = send(sockfd, buffer, bytes_read, 0);
        if (bytes_sent < 0) {
            perror("Erro ao enviar dados");
            break;
        }

        FILE *part = fopen(part_file, "ab");
        fwrite(buffer, 1, bytes_sent, part);
        fclose(part);
        usleep(500000); 
    }

    if (send(sockfd, "END", strlen("END"), 0) < 0) {
        perror("Erro ao enviar o END");
    }

    fclose(file);
    close(sockfd);

    if (bytes_read == 0) {
        printf("Transferência concluída.\n");
        if (remove(part_file) == 0) {
            printf("Arquivo parcial removido: %s\n", part_file);
        } else {
            perror("Erro ao remover o arquivo parcial");
        }
    } else {
        printf("Transferência interrompida. Arquivo parcial mantido: %s\n", part_file);
    }
}


int main(int argc, char *argv[]) {
    if (argc != 4) {
        fprintf(stderr, "Uso: %s <arquivo> <ip_servidor> <caminho_destino>\n", argv[0]);
        exit(EXIT_FAILURE);
    }

    send_file(argv[1], argv[2], 8080, argv[3]);
    return 0;
}
