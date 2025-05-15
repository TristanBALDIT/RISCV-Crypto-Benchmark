//
// Created by trist on 15/05/2025.
//
#include <stdint.h>
#include <stdio.h>
//#include "util.h"

int main ()
{
    uint32_t w_high = 0x11223344;
    uint32_t w_low = 0x55667788;
    uint32_t result;

    printf("High word");
    printf("%08X ", w_high );
    printf("Low word");
    printf("%08X ", w_low );

    asm volatile (
        "mv a0, %[hw]\n\t"
        "mv a1, %[lw]\n\t"
        ".word 0x04B5060B\n\t"
        "mov %[res], r0\n\t"
        : [res] "=r" (result)
        : [hw] "r"(w_high), [lw] "r"(w_low)
        : "r0", "r1", "r2"
    );

    printf("High word after ROR64");
    printf("%08X ", result);

    return 0;
}