#include <stdio.h>
#include <stdint.h>

static const uint8_t flag_xor[] = {
    11, 27, 22, 51, 40, 34, 41, 44, 53, 23,
    55, 63, 58, 16, 61, 41, 59, 53, 37, 46,
    36, 33, 44, 49, 53
};

static const char *key = "HOP";

static void mostrar_introducao(void) {
    puts("===============================================");
    puts(" Bem-vinda ao console lilás da Grace Hopper   ");
    puts("===============================================");
    puts("\033[95mUm navio no porto está seguro, mas não é para isso que os navios foram feitos.\033[0m");
    puts("\033[95mAnalise este programa com curiosidade de compiladora.\033[0m");
}

static void exibir_linha_do_tempo(void) {
    puts("Linha do tempo relâmpago:");
    puts("- 1944: Hopper ajuda a traduzir equações no Mark I.");
    puts("- 1952: O A-0 ganha vida para automatizar cartões perfurados.");
    puts("- 1959: O COBOL leva clareza às empresas.");
    puts("- Presente: você decifra mensagens escondidas em seções de dados.");
}

int main(void) {
    mostrar_introducao();
    exibir_linha_do_tempo();

    puts("\nDica: \033[95muse objdump ou strings, mas não confie em saídas óbvias.\033[0m");
    puts("Procure uma mensagem cifrada com XOR em algum lugar da memória somente leitura.");

    uint8_t acumulador = 0;
    for (size_t i = 0; i < sizeof flag_xor; ++i) {
        acumulador ^= flag_xor[i];
    }

    printf("Checksum temático: 0x%02x\n", acumulador);
    puts("Quando você desfizer a cifra, encontrará um tributo carinhoso à Dama dos Compiladores.");

    return 0;
}
