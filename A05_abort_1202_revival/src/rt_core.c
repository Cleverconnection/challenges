#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

typedef struct {
    const char *nome;
    int prioridade;
    int carga;
} tarefa_t;

void *executar_tarefa(void *arg) {
    tarefa_t *tarefa = (tarefa_t *)arg;
    for (int i = 0; i < tarefa->carga; i++) {
        usleep(5000);
    }
    pthread_exit(NULL);
}

int ler_variavel(const char *nome, int padrao) {
    const char *valor = getenv(nome);
    if (!valor) {
        return padrao;
    }
    return atoi(valor);
}

int main(void) {
    int prioridade_nav = ler_variavel("NAV_PRIORITY", 4);
    int prioridade_dsky = ler_variavel("DSKY_PRIORITY", 3);
    int carga_interruptores = ler_variavel("TASK_BURST", 120);

    tarefa_t tarefas[3] = {
        {"NAV_SAFE", prioridade_nav, 40},
        {"DSKY_UPDATE", prioridade_dsky, 30},
        {"RANDOM_LOAD", 6, carga_interruptores}
    };

    pthread_t threads[3];

    for (int i = 0; i < 3; i++) {
        pthread_create(&threads[i], NULL, executar_tarefa, &tarefas[i]);
    }

    for (int i = 0; i < 3; i++) {
        pthread_join(threads[i], NULL);
    }

    printf("Resumo: NAV=%d DSKY=%d BURST=%d\n", prioridade_nav, prioridade_dsky, carga_interruptores);

    if (prioridade_nav > prioridade_dsky || prioridade_nav > 2 || carga_interruptores > 80) {
        printf("ABORT 1202 detectado. Reconfigure prioridades imediatamente.\n");
        return 1202;
    }

    printf("CTF{abort_1202_superado}\n");
    return 0;
}
