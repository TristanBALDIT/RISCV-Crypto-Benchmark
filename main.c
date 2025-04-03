#include <stdio.h>
#include <stdint.h>
#include <stddef.h>
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

    //Know test vector for AES-GCM

    uint32_t aes_gcm_test_key[4] = {0x00000000, 0x00000000, 0x00000000, 0x00000000};
    uint32_t aes_gcm_test_iv[3] = {0x00000000, 0x00000000, 0x00000000};
    uint32_t aes_gcm_test_block[4] = {0x00000000, 0x00000000, 0x00000000, 0x00000000};
    uint32_t aes_gcm_test_ad[4];
    size_t aes_gcm_test_num_blocks = 1;
    size_t aes_gcm_test_num_ad_blocks = 0;

    // Data generation for AES/CHACHA
    uint32_t *key  = generate_random_32bit_words(8);
    uint32_t *block_10 = generate_random_32bit_words(360);
    uint32_t *ad_block_10 = generate_random_32bit_words(360);
    uint32_t *iv = generate_random_32bit_words(4);
    uint32_t *nonce = generate_random_32bit_words(3);

    uint64_t ce;
    uint64_t cd;
    uint64_t iterations = 100;

                            /* AES BENCHMARK */

    printf("AES BENCHMARK \n\n");

    initialize_aes_sbox();
    printf("Simple Block Encryption-Decryption\n\n");

    // AES EBC 1 Block - 100 iterations
    for(int i = 4; i < 10; i+=2)
    {
        ce =0, cd = 0;
        printf("KEY SIZE : %d \n", 32*i);
        for (int e = 0; e < iterations; e++)
        {
            if (e == 0)
            {
                printf("Plaintext :");
                print_state(test_state);
            }

            //instret_e = -read_csr(minstret);
            //cycles_e = -read_csr(mcycle);

            encryptBlock(test_state, test_key, i);

            //instret += read_csr(minstret);
            //cycles += read_csr(mcycle);
            //ce += cycles;

            if (e == 0)
            {
                printf("Ciphertext :");
                print_state(test_state);
                //printf("%d instructions\n", (int)(instret));
                //printf("%d cycles\n\n", (int)(cycles));
            }

            //instret_e = -read_csr(minstret);
            //cycles_e = -read_csr(mcycle);

            decryptBlock(test_state, test_key, i);

            //instret += read_csr(minstret);
            //cycles += read_csr(mcycle);
            //cd += cycles;

            if (e == 0)
            {
                printf("Final Plaintext :");
                print_state(test_state);
                //printf("%d instructions\n", (int)(instret));
                //printf("%d cycles\n\n", (int)(cycles));
            }
        }
        printf("Total cycles for %llu iterations :\n", iterations);
        printf("Encryption : %llu \n", ce);
        printf("Decryption : %llu \n\n\n", cd);
    }


    printf("AES-ECB 10 Blocks\n");


    for(int i=4; i < 10; i+=2)
    {
        ce =0, cd = 0;
        printf("KEY SIZE : %d \n", 32*i);
        for(int e = 0; e < iterations; e++)
        {

            //instret = -read_csr(minstret);
            //cycles = -read_csr(mcycle);

            for(int j=0; j < 10; j++)
            {
                encryptBlock(test_state, test_key, i);
            }

            //instret += read_csr(minstret);
            //cycles += read_csr(mcycle);
            //ce += cycles;

            if(e == 0)
            {
                //printf("Encryption : \n");
                //printf("%d instructions\n", (int)(instret));
                //printf("%d cycles\n\n", (int)(cycles));
            }

            //instret = -read_csr(minstret);
            //cycles = -read_csr(mcycle);

            for(int j=0; j < 10; j++)
            {
                decryptBlock(test_state, test_key, i);
            }

            //instret += read_csr(minstret);
            //cycles += read_csr(mcycle);
            //cd += cycles;

            if(e == 0)
            {
                //printf("Decryption : \n");
                //printf("%d instructions\n", (int)(instret));
                //printf("%d cycles\n\n", (int)(cycles));
            }

        }
        printf("Total cycles for %llu iterations :\n", iterations);
        printf("Encryption : %llu \n", ce);
        printf("Decryption : %llu \n\n\n", cd);
    }



    printf("AES-CBC 10 Blocks\n");

    for(int i=4; i < 10; i+=2)
    {
        ce =0, cd = 0;
        printf("KEY SIZE : %d \n", 32*i);
        for(int e=0; e < iterations; e++)
        {
            //instret = -read_csr(minstret);
            //cycles = -read_csr(mcycle);

            aes_cbc_encrypt(block_10, 10, key, iv, i);

            //instret += read_csr(minstret);
            //cycles += read_csr(mcycle);
            //ce += cycles;

            if(e == 0)
            {
                //printf("Encryption : \n");
                //printf("%d instructions\n", (int)(instret));
                //printf("%d cycles\n\n", (int)(cycles));
            }

            //instret = -read_csr(minstret);
            //cycles = -read_csr(mcycle);

            aes_cbc_decrypt(block_10, 10, key, iv, i);

            //instret += read_csr(minstret);
            //cycles += read_csr(mcycle);
            //cd += cycles;

            if(e == 0)
            {
                //printf("Decryption : \n");
                //printf("%d instructions\n", (int)(instret));
                //printf("%d cycles\n\n", (int)(cycles));
            }
        }
        printf("Total cycles for %llu iterations :\n", iterations);
        printf("Encryption : %llu \n", ce);
        printf("Decryption : %llu \n\n\n", cd);
    }

    printf("AES-CTR 10 Blocks\n");

    for(int i=4; i < 10; i+=2)
    {
        ce =0, cd = 0;
        printf("KEY SIZE : %d \n", 32*i);
        for(int e=0; e < iterations; e++)
        {
            //instret = -read_csr(minstret);
            //cycles = -read_csr(mcycle);

            aes_ctr(block_10, 10, key, iv, i);

            //instret += read_csr(minstret);
            //cycles += read_csr(mcycle);
            //ce += cycles;

            if(e == 0)
            {
                //printf("Encryption - Decryption : \n");
                //printf("%d instructions\n", (int)(instret));
                //printf("%d cycles\n\n", (int)(cycles));
            }

        }
        printf("Total cycles for %llu iterations :\n", iterations);
        printf("Encryption - Decryption : %llu \n\n\n", ce);
    }

    printf("AES-GCM Test Vector\n");

    uint32_t Test_mac[4];
    aes_gcm(aes_gcm_test_block,aes_gcm_test_ad,1,0,aes_gcm_test_key,aes_gcm_test_iv,4,Test_mac);

    printf("MAC :");
    print_state(Test_mac);

    printf("AES-GCM 10 Blocks\n");

    uint32_t T[4];
    for(int i=4; i < 10; i+=2)
    {
        ce =0, cd = 0;
        printf("KEY SIZE : %d \n", 32*i);
        for(int e = 0; e < iterations; e++)
        {
            //instret = -read_csr(minstret);
            //cycles = -read_csr(mcycle);

            aes_gcm(block_10, ad_block_10, 10, 10, key, iv, i, T);

            //instret += read_csr(minstret);
            //cycles += read_csr(mcycle);
            //ce += cycles;

            if(e == 0)
            {
                //printf("Encryption - Decryption : \n");
                //printf("%d instructions\n", (int)(instret));
                //printf("%d cycles\n\n", (int)(cycles));
            }
        }
        printf("Total cycles for %llu iterations :\n", iterations);
        printf("Encryption - Decryption : %llu \n\n\n", ce);
    }


                    /* Chacha20 BENCHMARK */

    printf("ChaCha20 Benchmark\n\n");

    // KeyBlock Test Vector Verification + 1 Block Benchmark
    printf("ChaCha20 KeyBlock Test Vector Verification & 1 Block benchmark\n\n");

    ce =0, cd = 0;
    for(int e = 0; e < iterations; e++)
    {
        uint32_t counter = e+1;
        uint32_t block[16];

        //instret = -read_csr(minstret);
        //cycles = -read_csr(mcycle);

        KeyBlockGeneration(block, chacha_test_key, test_nonce, counter);

        //instret += read_csr(minstret);
        //cycles += read_csr(mcycle);
        //ce += cycles;

        if(e == 0)
        {
            //printf("Chacha20 1 Block : \n");
            //printf("%d instructions\n", (int)(instret));
            //printf("%d cycles\n\n", (int)(cycles));
            print_chacha_block(block);
        }
    }
    printf("Total cycles for %llu iterations :\n", iterations);
    printf("Encryption - Decryption : %llu \n\n\n", ce);

    //Poly1305 Test Vector
    test_poly1305();

    printf("ChaCha20 10 Blocs \n\n");

    ce =0, cd = 0;
    for(int e = 0; e < iterations; e++)
    {
        //instret = -read_csr(minstret);
        //cycles = -read_csr(mcycle);

        Chacha20(block_10, key, nonce, 10);

        //instret += read_csr(minstret);
        //cycles += read_csr(mcycle);
        //ce += cycles;

        if(e == 0)
        {
            //printf("Chacha20 10 Block : \n");
            //printf("%d instructions\n", (int)(instret));
            //printf("%d cycles\n\n", (int)(cycles));
        }
    }
    printf("Total cycles for %llu iterations :\n", iterations);
    printf("Encryption - Decryption : %llu \n\n\n", ce);

    printf("ChaCha20-Poly1305 10 Blocs \n\n");

    uint8_t mac[16];

    for(int e = 0; e < iterations; e++)
    {
        //instret = -read_csr(minstret);
        //cycles = -read_csr(mcycle);

        Chacha20_Poly1305(block_10, ad_block_10, key, nonce, 10, 10, mac);

        //instret += read_csr(minstret);
        //cycles += read_csr(mcycle);
        //ce += cycles;

        if(e == 0)
        {
            //printf("Chacha20-Poly1305 10 Block : \n");
            //printf("%d instructions\n", (int)(instret));
            //printf("%d cycles\n\n", (int)(cycles));
        }
    }
    printf("Total cycles for %llu iterations :\n", iterations);
    printf("Encryption - Decryption : %llu \n\n\n", ce);

                    /* ASCON BENCHMARK */

    uint64_t ciphertext[20];
    uint64_t tag[2];
    uint64_t *plaintext = generate_random_64bit_words(20);
    uint64_t *key_ascon = generate_random_64bit_words(2);
    uint64_t *nonce_ascon = generate_random_64bit_words(2);
    uint64_t *ad_data = generate_random_64bit_words(10);
    uint64_t result[20];

    printf("ASCON_128 Test Vector / 10 Blocs\n\n");

    ce =0, cd = 0;
    for (int e = 0; e < iterations; e++)
    {
        if(e == 0)
        {
            printf("plain\n");
            for (int i = 0; i < 10; i++)
            {
                printf("%016llX ", plaintext[i]);
            }
            printf("\n");
        }

        //instret = -read_csr(minstret);
        //cycles = -read_csr(mcycle);

        ASCON_128_encrypt(plaintext, key_ascon, nonce_ascon, ad_data, 640, 320, ciphertext, tag);

        //instret += read_csr(minstret);
        //cycles += read_csr(mcycle);
        //ce += cycles;

        if(e == 0)
        {
            //printf("ASCON 10 Block Encrypt: \n");
            //printf("%d instructions\n", (int)(instret));
            //printf("%d cycles\n\n", (int)(cycles));
            printf("cipher\n");
            for (int i = 0; i < 10; i++)
            {
                printf("%016llX ", ciphertext[i]);
            }
            printf("\n");
        }

        //instret = -read_csr(minstret);
        //cycles = -read_csr(mcycle);

        ASCON_128_decrypt(result, key_ascon, nonce_ascon, ad_data, 640, 320, ciphertext, tag);

        //instret += read_csr(minstret);
        //cycles += read_csr(mcycle);
        //cd += cycles;

        if(e == 0)
        {
            //printf("ASCON_128 10 Blocks Decrypt : \n");
            //printf("%d instructions\n", (int)(instret));
            //printf("%d cycles\n\n", (int)(cycles));
            printf("plain \n");
            for (int i = 0; i < 10; i++)
            {
                printf("%016llX ", result[i]);
            }
            printf("\n");
        }
    }
    printf("Total cycles for %llu iterations :\n", iterations);
    printf("Encryption : %llu \n", ce);
    printf("Decryption : %llu \n\n\n", cd);


    printf("ASCON_128a 10 Blocks\n\n");

    ce =0, cd = 0;
    for(int e = 0; e < iterations; e++)
    {
        //instret = -read_csr(minstret);
        //cycles = -read_csr(mcycle);

        ASCON_128a_encrypt(plaintext, key_ascon, nonce_ascon, ad_data, 1280, 640, ciphertext, tag);

        //instret += read_csr(minstret);
        //cycles += read_csr(mcycle);
        //ce += cycles;

        if(e == 0)
        {
            //printf("ASCON_128a 10 Block Encrypt: \n");
            //printf("%d instructions\n", (int)(instret));
            //printf("%d cycles\n\n", (int)(cycles));
        }

        //instret = -read_csr(minstret);
        //cycles = -read_csr(mcycle);

        ASCON_128a_decrypt(result, key_ascon, nonce_ascon, ad_data, 1280, 640, ciphertext, tag);

        //instret += read_csr(minstret);
        //cycles += read_csr(mcycle);
        //cd += cycles;

        if(e == 0)
        {
            //printf("ASCON_128a 10 Blocks Decrypt : \n");
            //printf("%d instructions\n", (int)(instret));
            //printf("%d cycles\n\n", (int)(cycles));
        }
    }
    printf("Total cycles for %llu iterations :\n", iterations);
    printf("Encryption : %llu \n", ce);
    printf("Decryption : %llu \n\n\n", cd);

    //Free
    free(key);
    free(block_10);
    free(ad_block_10);
    free(nonce);
    free(iv);
    free(plaintext);
    free(key_ascon);
    free(nonce_ascon);
    free(ad_data);

    return 0;
}

