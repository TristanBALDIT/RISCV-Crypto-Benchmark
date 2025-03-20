//
// Created by trist on 18/03/2025.
//

#include "chacha.h"

#include <stdio.h>
#include <string.h>

void QR(uint32_t *a, uint32_t *b, uint32_t *c, uint32_t *d)
{
    *a += *b; *d ^= *a; *d = ROTL32(*d, 16);
    *c += *d; *b ^= *c; *b = ROTL32(*b, 12);
    *a += *b; *d ^= *a; *d = ROTL32(*d, 8);
    *c += *d; *b ^= *c; *b = ROTL32(*b, 7);

}

void KeyBlockGeneration(uint32_t block[16], uint32_t key[8], uint32_t nonce[3], uint32_t counter)
{
    block[0] = CHACHA_CONST_0;
    block[1] = CHACHA_CONST_1;
    block[2] = CHACHA_CONST_2;
    block[3] = CHACHA_CONST_3;

    memcpy(&block[4], key, 8 * sizeof(uint32_t));
    block[12] = counter;
    memcpy(&block[13], nonce, 3 * sizeof(uint32_t));

    for (int i = 0; i < 16; i++)
    {
        if (i % 4 == 0)
        {
            printf("\n");
        }
        printf("%08X ", block[i]);
    }
    printf("\n");

    uint32_t working_block[16];
    memcpy(working_block, block, 16*sizeof(uint32_t));

    for (int i = 0; i < 10; i++) { // 10 double rounds = 20 rounds
        // Column rounds
        QR(&working_block[0], &working_block[4], &working_block[8], &working_block[12]);
        QR(&working_block[1], &working_block[5], &working_block[9], &working_block[13]);
        QR(&working_block[2], &working_block[6], &working_block[10], &working_block[14]);
        QR(&working_block[3], &working_block[7], &working_block[11], &working_block[15]);

        // Diagonal rounds
        QR(&working_block[0], &working_block[5], &working_block[10], &working_block[15]);
        QR(&working_block[1], &working_block[6], &working_block[11], &working_block[12]);
        QR(&working_block[2], &working_block[7], &working_block[8], &working_block[13]);
        QR(&working_block[3], &working_block[4], &working_block[9], &working_block[14]);
    }

    for (int i = 0; i < 16; i++)
    {
        if (i % 4 == 0)
        {
            printf("\n");
        }
        printf("%08X ", working_block[i]);
    }
    printf("\n");

    for (int i = 0; i < 16; i++) block[i] += working_block[i];
}