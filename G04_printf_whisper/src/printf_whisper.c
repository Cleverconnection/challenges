#include <stdio.h>
#include <string.h>

static const char lilas_banner[] =
    "\033[95m\"A linguagem mais poderosa é aquela que qualquer pessoa consegue ler.\"\033[0m";
static const char lilas_flag[] = "CTF{grace_printf_confiança}";

int main(void) {
    char buffer[256];

    puts("===============================================");
    puts(" Estação de Eco Lilás — Format String Training ");
    puts("===============================================");
    puts(lilas_banner);
    puts("Fale com o compilador fantasma de Hopper. Ele repete exatamente o que você manda.");
    puts("Envie sequências de formato para espiar a memória da embarcação.\n");

    while (1) {
        fputs("mensagem lilás> ", stdout);
        fflush(stdout);

        if (!fgets(buffer, sizeof buffer, stdin)) {
            puts("Até logo, cadete.");
            break;
        }

        buffer[strcspn(buffer, "\n")] = '\0';

        printf(buffer, lilas_flag, &buffer);
        putchar('\n');
    }

    return 0;
}
