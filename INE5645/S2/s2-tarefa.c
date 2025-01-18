#include <stdio.h>
#include <pthread.h>
#include <unistd.h>
#include <ctype.h>

#define N_THREADS 5   

int ERRO_TH = 111;
int SUCESSO_TH = 222;

pthread_t minhas_threads[N_THREADS]; // Identificadores para as threads

/** Função executada pelas threads */
void* codigo_tarefa(void* nome) {
    char* nome_thread = (char*) nome; // Conversão do ponteiro recebido
    for (int ns = 0; ns < 10; ++ns) {
        sleep(1); // Dorme 1 segundo por iteração
        printf("Tarefa %s: passaram %d segundos do total de 10.\n", nome_thread, ns + 1);
    }
    
    if (isupper(nome_thread[0])) {
        pthread_exit((void*)&SUCESSO_TH); // Retorna ponteiro para SUCESSO_TH
    }    
    pthread_exit((void*)&ERRO_TH); // Retorna ponteiro para ERRO_TH
}

/** Função principal, cria as threads */
int main(void) {
    char *param_threads[N_THREADS] = {
        "Rafa", "gustavo", "Tanara", "aurelio", "Barbara"
    };
    int* retornos[N_THREADS]; // Armazena os retornos das threads

    printf("Inicio\n");

    // Cria todas as threads
    for (int i = 0; i < N_THREADS; ++i) {
        pthread_create(&minhas_threads[i], NULL, codigo_tarefa, (void*) param_threads[i]);
    }

    // Espera por todas as threads
    for (int i = 0; i < N_THREADS; ++i) {
        pthread_join(minhas_threads[i], (void**)&retornos[i]);
        printf("Thread %s terminou com retorno %d\n", param_threads[i], *(int*)retornos[i]);
    }

    printf("Fim\n");
    return 0;
}
