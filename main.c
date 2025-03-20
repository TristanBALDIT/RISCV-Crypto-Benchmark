#include <stdio.h>
#include <stdint.h>
#include <string.h>
#include "aes.h"
#include "chacha.h"

void print_state(uint32_t state[4])
{
    for (int j = 0; j < 4; j++)
    {
        printf("%08X ", state[j]);
    }
    printf("\n");
}


int main() {
    // Initialisation de la S-Box
    initialize_aes_sbox();

    // Clé d'exemple (128 bits = 16 octets)
    uint32_t key[4] = {0x2b7e1516, 0x28aed2a6, 0xabf71588, 0x09cf4f3c};

    // Bloc de texte clair (16 octets)
    uint32_t state[4] = {
        0x3243F6A8,
        0x885A308D,
        0x313198A2,
        0xE0370734
    };

    printf("Bloc en clair : ");
    print_state(state);

    encryptBlock(state, key, KEY_SIZE_128);

    printf("Bloc chiffre : ");
    print_state(state);

    decryptBlock(state, key, KEY_SIZE_128);

    printf("Bloc dechiffre : ");
    print_state(state);


    printf("\n\n");
    printf("ChaCha20");
    printf("\n\n");

    uint32_t chacha_key[8] = {0x03020100, 0x07060504, 0x0b0a0908, 0x0f0e0d0c,
    0x13121110, 0x17161514, 0x1b1a1918, 0x1f1e1d1c};
    uint32_t counter = 1;
    uint32_t nonce[3] = {0x09000000, 0x4a000000, 0x00000000};

    uint32_t block[16];
    KeyBlockGeneration(block, chacha_key, nonce, counter);

    for (int i = 0; i < 16; i++)
    {
        if (i % 4 == 0)
        {
            printf("\n");
        }
        printf("%08X ", block[i]);
    }

    return 0;
}

