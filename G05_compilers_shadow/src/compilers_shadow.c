#include <stdio.h>
#include <stdint.h>
#include <string.h>
#include <stdlib.h>
#include <errno.h>
#ifdef __linux__
#include <sys/ptrace.h>
#endif

static const uint8_t encoded_flag[] = {
    130, 140, 7, 148, 12, 7, 145, 21, 150, 134, 22, 20,
    145, 148, 155, 146, 8, 149, 27, 18, 154, 155, 154, 144,
    146, 22, 155, 149
};
static const uint8_t rotor[] = {3, 1, 4, 1, 5, 9};
static const char key[] = "HOPPER";

static int verificar_debug(void) {
#ifdef __linux__
    errno = 0;
    if (ptrace(PTRACE_TRACEME, 0, NULL, 0) == -1) {
        return -1;
    }
#endif
    return 0;
}

static void girar_decodificador(char *saida) {
    const size_t len = sizeof(encoded_flag) / sizeof(encoded_flag[0]);
    const size_t rotor_len = sizeof(rotor) / sizeof(rotor[0]);
    for (size_t i = 0; i < len; ++i) {
        uint8_t valor = (uint8_t)((encoded_flag[i] + rotor[i % rotor_len]) & 0xFF);
        valor = (uint8_t)(((valor << 1) | (valor >> 7)) & 0xFF);
        valor ^= (uint8_t)key[i % (sizeof key - 1)];
        saida[i] = (char)valor;
    }
    saida[len] = '\0';
}

static int calcular_meta(void) {
    const char *palavra = "FLOWMATIC";
    int acumulador = 0x1F;
    for (size_t i = 0; palavra[i] != '\0'; ++i) {
        acumulador ^= (unsigned char)palavra[i];
        acumulador = ((acumulador << 3) | (acumulador >> 13)) & 0xFFFF;
        acumulador += 7;
    }
    return acumulador & 0xFFF;
}

static void banner(void) {
    puts("====================================================");
    puts(" Câmara Lilás — Protótipo do Compilador Sombra ");
    puts("====================================================");
    puts("\033[95m\"Um navio no porto está seguro, mas não é para isso que navios foram feitos.\"\033[0m");
    puts("\033[95mPara navegar, descubra o protocolo que ativa o rotor secreto.\033[0m\n");
}

static void limpar_linha(char *linha) {
    size_t n = strlen(linha);
    if (n && linha[n - 1] == '\n') {
        linha[n - 1] = '\0';
    }
}

int main(void) {
    if (verificar_debug() == -1) {
        puts("Intruso detectado. A sombra do compilador não tolera depuradores.");
        return 1;
    }

    banner();

    enum {ESTADO_INICIO, ESTADO_PREPARO, ESTADO_LANCAMENTO, ESTADO_FINAL} estado = ESTADO_INICIO;
    char linha[128];
    int tentativas = 0;

    while (estado != ESTADO_FINAL && tentativas < 7) {
        fputs("comando lilás> ", stdout);
        fflush(stdout);
        if (!fgets(linha, sizeof linha, stdin)) {
            puts("Encerrando protocolo.");
            return 0;
        }
        limpar_linha(linha);
        ++tentativas;

        switch (estado) {
            case ESTADO_INICIO:
                if (strcmp(linha, "iniciar compilador") == 0) {
                    puts("Estado atualizado: analisador sintático em preparação.");
                    estado = ESTADO_PREPARO;
                } else {
                    puts("Sequência inválida. Lembre-se das palavras usadas por Hopper ao ligar o Mark I.");
                }
                break;
            case ESTADO_PREPARO:
                if (strcmp(linha, "executar a-0") == 0) {
                    puts("Estado atualizado: otimizador aguardando senha.");
                    estado = ESTADO_LANCAMENTO;
                } else {
                    puts("O compilador espera a referência ao A-0 antes de continuar.");
                }
                break;
            case ESTADO_LANCAMENTO:
                if (strcmp(linha, "otimizar rotina") == 0) {
                    puts("Rotor inicializado. Informe o token numérico.");
                    estado = ESTADO_FINAL;
                } else {
                    puts("Sem a palavra-chave de otimização, o rotor não gira.");
                }
                break;
            default:
                break;
        }
    }

    if (estado != ESTADO_FINAL) {
        puts("O compilador sombra retornou ao modo seguro.");
        return 0;
    }

    fputs("token lilás> ", stdout);
    fflush(stdout);
    if (!fgets(linha, sizeof linha, stdin)) {
        puts("Sequência abortada.");
        return 0;
    }
    limpar_linha(linha);

    char *fim = NULL;
    errno = 0;
    long valor = strtol(linha, &fim, 10);
    if (errno != 0 || fim == linha || *fim != '\0') {
        puts("Token inválido. O somador de Hopper não reconheceu o formato.");
        return 0;
    }

    if (valor != calcular_meta()) {
        puts("Token incorreto. Estude o algoritmo FLOWMATIC.");
        return 0;
    }

    char saida[sizeof encoded_flag + 1];
    girar_decodificador(saida);
    printf("Canal liberado: %s\n", saida);
    return 0;
}
