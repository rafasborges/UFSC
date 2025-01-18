#include <stdio.h>
#include <unistd.h>
#include <pthread.h>
#include <stdlib.h>


pthread_t t1;	// Identificador da thread t1
pthread_t t2;	// Identificador da thread t2 


double saldo = 10000.0;		// Saldo inicial de 10 mil reais


/** Faz 100 retiradas de 10 reais */
void codigo_tarefa_1(void){
	double saldo_velho;
	double saldo_novo;
	sleep(1);	// Faz alguma inicializacao
	for( int ns=0; ns < 100; ++ns) {
		saldo_velho = saldo;
		saldo_novo = saldo_velho - 10;
		printf("Saldo passou de %0.2lf para o valor de %0.2lf\n", saldo_velho, saldo_novo);
		saldo = saldo_novo;
	}
}


/** Faz 100 depositos de 10 reais */
void codigo_tarefa_2(void){
	double saldo_velho;
	double saldo_novo;
	sleep(1);	// Faz alguma inicializacao
	for( int ns=0; ns < 100; ++ns) {
		saldo_velho = saldo;
		saldo_novo = saldo_velho + 10;
		printf("Saldo passou de %0.2lf para o valor de %0.2lf\n", saldo_velho, saldo_novo);
		saldo = saldo_novo;
	}
}


/** Função principal, cria as threads */
int main(void){
	printf("Inicio\n");
	printf("Saldo inicial %0.2lf\n", saldo);

	//codigo_tarefa_1();
	//codigo_tarefa_2();

	pthread_create(&t1, NULL, (void *) codigo_tarefa_1, NULL);
	pthread_create(&t2, NULL, (void *) codigo_tarefa_2, NULL);

	pthread_join(t1, NULL);
	pthread_join(t2, NULL);

	printf("Saldo final ficou %0.2lf\n", saldo);

	printf("Fim\n");
	return(0);
}



