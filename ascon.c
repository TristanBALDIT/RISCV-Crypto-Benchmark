//
// Created by trist on 24/03/2025.
//
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include "ascon.h"

uint64_t rc[12] = {
    0x00000000000000f0, 0x00000000000000e1, 0x00000000000000d2,
    0x00000000000000c3, 0x00000000000000b4, 0x00000000000000a5,
    0x0000000000000096, 0x0000000000000087, 0x0000000000000078,
    0x0000000000000069, 0x000000000000005a, 0x000000000000004b
};

void p(uint64_t state[5], uint64_t n)
{
    for(int i = 0; i < n; i++)
    {
        state[2] ^= rc[i];

        uint64_t temp[5];
        state[0] ^= state[4], state[4] ^= state[3], state[2] ^= state[1];
        temp[0] = state[0], temp[1] = state[1], temp[2] = state[2], temp[3] = state[3], temp[4] = state[4];
        temp[0] =~ temp[0], temp[1] =~  temp[1], temp[2] =~  temp[2], temp[3] =~ temp[3], temp[4] =~ temp[4];
        temp[0] &= state[1], temp[1] &= state[2], temp[2] &= state[3], temp[3] &= state[4], temp[4] &= state[0];
        state[0] ^= temp[1], state[1] ^= temp[2], state[2] ^= temp[3], state[3] ^= temp[4], state[4] ^= state[0];
        state[1] ^= state[0], state[0] ^= state[4], state[3] ^= state[2], state[2] =~ state[2];

        state[0] = state[0] ^ ROR64(state[0], 19) ^ ROR64(state[0], 28);
        state[1] = state[1] ^ ROR64(state[1], 61) ^ ROR64(state[1], 39);
        state[2] = state[2] ^ ROR64(state[2], 1) ^ ROR64(state[2], 6);
        state[3] = state[3] ^ ROR64(state[3], 10) ^ ROR64(state[3], 17);
        state[4] = state[4] ^ ROR64(state[4], 7) ^ ROR64(state[4], 41);
    }
}

void ASCON_128_encrypt(uint64_t *data, const uint64_t key[2], const uint64_t nonce[2], uint64_t *ad_data,
    const size_t len_data, const size_t len_ad_data, uint64_t *ciphertext, uint64_t *tag)
{
    size_t l = len_data % 64;
    size_t n = len_ad_data % 64;

    size_t num_blocks = len_data / 64;
    size_t num_ad_blocks = len_ad_data / 64;

    if (l != 0)
    {
        data[num_blocks-1] = (data[num_blocks-1] << (64-l)) | (0x1 << (63-l));
    }
    if(n != 0)
    {
        ad_data[num_ad_blocks-1] = (ad_data[num_ad_blocks-1] << (64-n)) | (0x1 << (63-n));
    }

    uint64_t state[5];
    state[0] = 0x80400c0600000000;
    state[1] = key[0];
    state[2] = key[2];
    state[3] = nonce[0];
    state[4] = nonce[1];

    p(state, 12);
    state[0] ^= 0x0000000000000000;
    state[1] ^= 0x0000000000000000;
    state[2] ^= 0x0000000000000000;
    state[3] ^= key[0];
    state[4] ^= key[1];

    for(int i = 0; i < num_ad_blocks; i++)
    {
        state[0] ^= ad_data[i];
        p(state,6);
    }
    state[4] ^= 0x0000000000000001;

    for(int i = 0; i < num_blocks-1; i++)
    {
        state[0] ^= data[i];
        ciphertext[i] = state[0];
        p(state,6);
    }

    state[0] ^= data[num_blocks-1];
    if(l != 0)
    {
        ciphertext[num_blocks-1] = (state[0] >> (64-l));
    }
    else
    {
        ciphertext[num_blocks-1] = state[0];
    }

    state[1] ^= key[0];
    state[2] ^= key[1];
    p(state, 12);

    tag[0] = state[3] ^ key[0];
    tag[1] = state[4] ^ key[1];

}

void ASCON_128_decrypt(uint64_t *data, const uint64_t key[2], const uint64_t nonce[2], uint64_t *ad_data,
    const size_t len_data, const size_t len_ad_data, uint64_t *ciphertext, uint64_t *tag)
{
    size_t l = len_data % 64;
    size_t n = len_ad_data % 64;

    size_t num_blocks = len_data / 64;
    size_t num_ad_blocks = len_ad_data / 64;

    if(n != 0)
    {
        ad_data[num_ad_blocks-1] = (ad_data[num_ad_blocks-1] << (64-n)) | (0x1 << (63-n));
    }

    uint64_t state[5];
    state[0] = 0x80400c0600000000;
    state[1] = key[0];
    state[2] = key[2];
    state[3] = nonce[0];
    state[4] = nonce[1];

    p(state, 12);
    state[0] ^= 0x0000000000000000;
    state[1] ^= 0x0000000000000000;
    state[2] ^= 0x0000000000000000;
    state[3] ^= key[0];
    state[4] ^= key[1];

    for(int i = 0; i < num_ad_blocks; i++)
    {
        state[0] ^= ad_data[i];
        p(state,6);
    }
    state[4] ^= 0x0000000000000001;

    for(int i = 0; i < num_blocks-1; i++)
    {
        data[i] = state[0] ^ ciphertext[i];
        state[0] = ciphertext[i];
        p(state,6);
    }

    if(l != 0)
    {
        data[num_blocks-1] = (state[0] >> (64-l)) ^ ciphertext[num_blocks-1];
        state[0] = (ciphertext[num_blocks-1] << (64-l) ) | ((state[0] & ((1ULL << 64-l) - 1)) ^ (0x1 << (63-l)));
    }
    else
    {
        data[num_blocks-1] = state[0] ^ ciphertext[num_blocks-1];
        state[0] = ciphertext[num_blocks-1];
    }

    state[1] ^= key[0];
    state[2] ^= key[1];
    p(state, 12);

    tag[0] = state[3] ^ key[0];
    tag[1] = state[4] ^ key[1];
}