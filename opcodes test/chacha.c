//
// Created by trist on 04/06/2025.
//
#include <stdint.h>
#include <stdio.h>
#include <inttypes.h>
//#include  "util.h"

int main()
{
    uint32_t r1 = 0x00000001;
    uint32_t r2 = 0x00000002;
    uint32_t r3 = 0x00000000;
    uint32_t result;

    printf("R1 : ");
    printf("%08" PRIX32 "\r\n", r1);
    printf("R2 : ");
    printf("%08" PRIX32 "\r\n", r2);
    printf("R3 : ");
    printf("%08" PRIX32 "\r\n", r3);

    asm volatile (
        ".insn r1 CUSTOM_0, 3, 0, %[rd], %[rs1], %[rs2], %[rs3]\n\t"
        : [rd] "=r" (result)
        : [rs1] "r" (r1), [rs2] "r" (r2), [rs3] "r" (r3)
    );

    printf("Result OP_CHACHA : ");
    printf("%08" PRIX32 "\r\n", result);
}
