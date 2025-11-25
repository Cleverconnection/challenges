#include <stdio.h>

const char memorial_grace[] = "CTF{grace_symbol_legivel}";

static void homenagear(void) {
    puts("===============================================");
    puts(" Laboratório Lilás — Mapa de Símbolos Visíveis ");
    puts("===============================================");
    puts("\033[95m\"Devemos escrever programas que possam ser lidos por humanos.\"\033[0m");
}

void exibir_manifesto(void) {
    puts("Manifesto da clareza compilada:");
    puts("1. Nomeie bem suas variáveis.");
    puts("2. Preserve símbolos quando ensinar novatas.");
    puts("3. Lembre-se da Almirante Hopper ao inspecionar tabelas.");
}

int main(void) {
    homenagear();
    exibir_manifesto();
    puts("\nExplore a tabela de símbolos e encontre o ponteiro comemorativo.");
    return 0;
}
