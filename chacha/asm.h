//
// Created by trist on 04/06/2025.
//

#ifndef ASM_H
#define ASM_H
#include <stdint.h>

#ifdef NO_RISCV_ASM

static inline uint32_t OP_CHACHA_16(uint32_t r1, uint32_t r2, uint32_t r3) {
    uint32_t result = (r1 + r2) ^ r3;
    return  (result << 16) | (result >> 16);
}

static inline uint32_t OP_CHACHA_12(uint32_t r1, uint32_t r2, uint32_t r3) {
    uint32_t result = (r1 + r2) ^ r3;
    return  (result << 12) | (result >> 20);
}

static inline uint32_t OP_CHACHA_8(uint32_t r1, uint32_t r2, uint32_t r3) {
    uint32_t result = (r1 + r2) ^ r3;
    return  (result << 8) | (result >> 24);
}

static inline uint32_t OP_CHACHA_7(uint32_t r1, uint32_t r2, uint32_t r3) {
    uint32_t result = (r1 + r2) ^ r3;
    return  (result << 7) | (result >> 25);
}

#else

static inline uint32_t OP_CHACHA_16(uint32_t r1, uint32_t r2, uint32_t r3) {
    uint32_t result;
    asm volatile (
    ".insn r4 CUSTOM_0, 3, 0, %[rd], %[rs1], %[rs2], %[rs3]\n\t"
    : [rd] "=r" (result)
    : [rs1] "r" (r1), [rs2] "r" (r2), [rs3] "r" (r3)
    );
    return result;
}

static inline uint32_t OP_CHACHA_12(uint32_t r1, uint32_t r2, uint32_t r3) {
    uint32_t result;
    asm volatile (
    ".insn r4 CUSTOM_0, 3, 1, %[rd], %[rs1], %[rs2], %[rs3]\n\t"
    : [rd] "=r" (result)
    : [rs1] "r" (r1), [rs2] "r" (r2), [rs3] "r" (r3)
    );
    return result;
}

static inline uint32_t OP_CHACHA_8(uint32_t r1, uint32_t r2, uint32_t r3) {
    uint32_t result;
    asm volatile (
    ".insn r4 CUSTOM_0, 3, 2, %[rd], %[rs1], %[rs2], %[rs3]\n\t"
    : [rd] "=r" (result)
    : [rs1] "r" (r1), [rs2] "r" (r2), [rs3] "r" (r3)
    );
    return result;
}

static inline uint32_t OP_CHACHA_7(uint32_t r1, uint32_t r2, uint32_t r3) {
    uint32_t result;
    asm volatile (
    ".insn r4 CUSTOM_0, 3, 3, %[rd], %[rs1], %[rs2], %[rs3]\n\t"
    : [rd] "=r" (result)
    : [rs1] "r" (r1), [rs2] "r" (r2), [rs3] "r" (r3)
    );
    return result;
}

#endif //NO_RISCV_ASM

#endif //ASM_H
