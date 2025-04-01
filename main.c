#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <string.h>
#include "aes/aes.h"
#include "chacha/chacha.h"
#include "chacha/poly1305.h"
#include  "loader.h"
#include "ascon.h"

void print_state(uint32_t state[4])
{
    for (int j = 0; j < 4; j++)
    {
        printf("%08X ", state[j]);
    }
    printf("\n");
}

void print_chacha_block(uint32_t block[16])
{
    for (int i = 0; i < 16; i++)
    {
        if (i % 4 == 0)
        {
            printf("\n");
        }
        printf("%08X ", block[i]);
    }
    printf("\n");
}


int main() {

                           /* KEY & BLOCKS GENERATION  */

    //size_t instret, cycles;

    // Known vector for AES
    uint32_t test_key[4] = {0x2b7e1516, 0x28aed2a6, 0xabf71588, 0x09cf4f3c};
    uint32_t test_state[4] = {
        0x3243F6A8,
        0x885A308D,
        0x313198A2,
        0xE0370734
    };

    // Known test vector for ChaCha20
    uint32_t chacha_test_key[8] = {
        0x03020100, 0x07060504, 0x0b0a0908, 0x0f0e0d0c,
        0x13121110, 0x17161514, 0x1b1a1918, 0x1f1e1d1c};
    uint32_t test_nonce[3] = {0x09000000, 0x4a000000, 0x00000000};

    // Data generation for AES/CHACHA
    uint32_t *key  = generate_random_32bit_words(8);
    uint32_t *block_10 = generate_random_32bit_words(360);
    uint32_t *ad_block_10 = generate_random_32bit_words(360);
    uint32_t *iv = generate_random_32bit_words(4);
    uint32_t *nonce = generate_random_32bit_words(3);

                            /* AES BENCHMARK */

    printf("AES BENCHMARK \n\n");

    printf("Simple Block Encryption-Decryption\n\n");
    initialize_aes_sbox();

    for(int i = 4; i < 10; i+=2)
    {
        printf("KEY SIZE : %d \n", 32*i);

        //instret = -read_csr(minstret);
        //cycles = -read_csr(mcycles);

        printf("Plaintext :");
        print_state(test_state);

        encryptBlock(test_state, test_key, i);

        //instret += read_csr(minstret);
        //cycles += read_csr(mcycles);

        printf("Ciphertext :");
        print_state(test_state);
        //printf("%d instructions\n", (int)(instret));
        //printf("%d cycles\n\n", (int)(cycles));

        decryptBlock(test_state, test_key, i);

        printf("Final Plaintext :");
        print_state(test_state);
        //printf("%d instructions\n", (int)(instret));
        //printf("%d cycles\n\n", (int)(cycles));
    }


    printf("AES-CBC 10 Blocks\n");

    for(int i=4; i < 10; i+=2)
    {
        printf("KEY SIZE : %d \n", 32*i);

        //instret = -read_csr(minstret);
        //cycles = -read_csr(mcycles);

        aes_cbc_encrypt(block_10, 10, key, iv, i);

        //instret += read_csr(minstret);
        //cycles += read_csr(mcycles);

        //printf("Encryption : \n");
        //printf("%d instructions\n", (int)(instret));
        //printf("%d cycles\n\n", (int)(cycles));

        //instret = -read_csr(minstret);
        //cycles = -read_csr(mcycles);

        aes_cbc_decrypt(block_10, 10, key, iv, i);

        //instret += read_csr(minstret);
        //cycles += read_csr(mcycles);

        //printf("Decryption : \n");
        //printf("%d instructions\n", (int)(instret));
        //printf("%d cycles\n\n", (int)(cycles));
    }


                    /* Chacha20 BENCHMARK */

    printf("ChaCha20 Benchmark\n\n");

    // KeybLock Test Vector Verification
    printf("ChaCha20 KeyBlock Test Vector Verification \n\n");

    uint32_t counter = 1;
    uint32_t block[16];

    //instret = -read_csr(minstret);
    //cycles = -read_csr(mcycles);

    KeyBlockGeneration(block, chacha_test_key, test_nonce, counter);

    //instret += read_csr(minstret);
    //cycles += read_csr(mcycles);

    //printf("Chacha20 1 Block : \n");
    //printf("%d instructions\n", (int)(instret));
    //printf("%d cycles\n\n", (int)(cycles));

    print_chacha_block(block);

    //Poly1305 Test Vector
    test_poly1305();

    printf("ChaCha20 10 Blocs \n\n");

    //instret = -read_csr(minstret);
    //cycles = -read_csr(mcycles);

    Chacha20(block_10, key, nonce, 10);

    //instret += read_csr(minstret);
    //cycles += read_csr(mcycles);

    //printf("Chacha20 10 Block : \n");
    //printf("%d instructions\n", (int)(instret));
    //printf("%d cycles\n\n", (int)(cycles));


    printf("ChaCha20-Poly1305 10 Blocs \n\n");

    uint8_t mac[16];

    //instret = -read_csr(minstret);
    //cycles = -read_csr(mcycles);

    Chacha20_Poly1305(block_10, ad_block_10, key, nonce, 10, 10, mac);

    //instret += read_csr(minstret);
    //cycles += read_csr(mcycles);

    //printf("Chacha20 10 Block : \n");
    //printf("%d instructions\n", (int)(instret));
    //printf("%d cycles\n\n", (int)(cycles));

    //Free
    free(key);
    free(block_10);
    free(ad_block_10);
    free(nonce);
    free(iv);


                    /* ASCON BENCHMARK */

    uint64_t ciphertext[10];
    uint64_t tag[2];
    uint64_t *plaintext = generate_random_64bit_words(10);
    uint64_t *key_ascon = generate_random_64bit_words(2);
    uint64_t *nonce_ascon = generate_random_64bit_words(2);
    uint64_t *ad_data = generate_random_64bit_words(5);
    uint64_t result[10];

    printf("plain\n");
    for (int i = 0; i < 10; i++)
    {
        printf("%016llX ", plaintext[i]);
    }
    printf("\n");
    ASCON_128_encrypt(plaintext, key_ascon, nonce_ascon, ad_data, 640, 320, ciphertext, tag);
    printf("cipher\n");
    for (int i = 0; i < 10; i++)
    {
        printf("%016llX ", ciphertext[i]);
    }
    printf("\n");
    ASCON_128_decrypt(result, key_ascon, nonce_ascon, ad_data, 640, 320, ciphertext, tag);
    printf("plain \n");
    for (int i = 0; i < 10; i++)
    {
        printf("%016llX ", result[i]);
    }
    printf("\n");
    return 0;
}

