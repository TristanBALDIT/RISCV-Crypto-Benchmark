//
// Created by trist on 16/05/2025.
//

#ifndef ASM_H
#define ASM_H

#include <stdint.h>

#ifdef NO_RISCV_ASM

static inline uint32_t custom_ROR64H_19(uint32_t w_high, uint32_t w_low) {
    uint64_t w = ((uint64_t)w_high << 32) | w_low;
    uint64_t r = (w >> 19) | (w << (64 - 19));
    return (uint32_t)(r >> 32);
}

static inline uint32_t custom_ROR64L_19(uint32_t w_high, uint32_t w_low) {
    uint64_t w = ((uint64_t)w_high << 32) | w_low;
    uint64_t r = (w >> 19) | (w << (64 - 19));
    return (uint32_t)(r);
}

static inline uint32_t custom_ROR64H_28(uint32_t w_high, uint32_t w_low) {
    uint64_t w = ((uint64_t)w_high << 32) | w_low;
    uint64_t r = (w >> 28) | (w << (64 - 28));
    return (uint32_t)(r >> 32);
}

static inline uint32_t custom_ROR64L_28(uint32_t w_high, uint32_t w_low) {
    uint64_t w = ((uint64_t)w_high << 32) | w_low;
    uint64_t r = (w >> 28) | (w << (64 - 28));
    return (uint32_t)(r);
}

static inline uint32_t custom_ROR64H_61(uint32_t w_high, uint32_t w_low) {
    uint64_t w = ((uint64_t)w_high << 32) | w_low;
    uint64_t r = (w >> 61) | (w << (64 - 61));
    return (uint32_t)(r >> 32);
}

static inline uint32_t custom_ROR64L_61(uint32_t w_high, uint32_t w_low) {
    uint64_t w = ((uint64_t)w_high << 32) | w_low;
    uint64_t r = (w >> 61) | (w << (64 - 61));
    return (uint32_t)(r);
}

static inline uint32_t custom_ROR64H_39(uint32_t w_high, uint32_t w_low) {
    uint64_t w = ((uint64_t)w_high << 32) | w_low;
    uint64_t r = (w >> 39) | (w << (64 - 39));
    return (uint32_t)(r >> 32);
}

static inline uint32_t custom_ROR64L_39(uint32_t w_high, uint32_t w_low) {
    uint64_t w = ((uint64_t)w_high << 32) | w_low;
    uint64_t r = (w >> 39) | (w << (64 - 39));
    return (uint32_t)(r);
}

static inline uint32_t custom_ROR64H_1(uint32_t w_high, uint32_t w_low) {
    uint64_t w = ((uint64_t)w_high << 32) | w_low;
    uint64_t r = (w >> 1) | (w << (64 - 1));
    return (uint32_t)(r >> 32);
}

static inline uint32_t custom_ROR64L_1(uint32_t w_high, uint32_t w_low) {
    uint64_t w = ((uint64_t)w_high << 32) | w_low;
    uint64_t r = (w >> 1) | (w << (64 - 1));
    return (uint32_t)(r);
}

static inline uint32_t custom_ROR64H_6(uint32_t w_high, uint32_t w_low) {
    uint64_t w = ((uint64_t)w_high << 32) | w_low;
    uint64_t r = (w >> 6) | (w << (64 - 6));
    return (uint32_t)(r >> 32);
}

static inline uint32_t custom_ROR64L_6(uint32_t w_high, uint32_t w_low) {
    uint64_t w = ((uint64_t)w_high << 32) | w_low;
    uint64_t r = (w >> 6) | (w << (64 - 6));
    return (uint32_t)(r);
}

static inline uint32_t custom_ROR64H_10(uint32_t w_high, uint32_t w_low) {
    uint64_t w = ((uint64_t)w_high << 32) | w_low;
    uint64_t r = (w >> 10) | (w << (64 - 10));
    return (uint32_t)(r >> 32);
}

static inline uint32_t custom_ROR64L_10(uint32_t w_high, uint32_t w_low) {
    uint64_t w = ((uint64_t)w_high << 32) | w_low;
    uint64_t r = (w >> 10) | (w << (64 - 10));
    return (uint32_t)(r);
}

static inline uint32_t custom_ROR64H_17(uint32_t w_high, uint32_t w_low) {
    uint64_t w = ((uint64_t)w_high << 32) | w_low;
    uint64_t r = (w >> 17) | (w << (64 - 17));
    return (uint32_t)(r >> 32);
}

static inline uint32_t custom_ROR64L_17(uint32_t w_high, uint32_t w_low) {
    uint64_t w = ((uint64_t)w_high << 32) | w_low;
    uint64_t r = (w >> 17) | (w << (64 - 17));
    return (uint32_t)(r);
}

static inline uint32_t custom_ROR64H_7(uint32_t w_high, uint32_t w_low) {
    uint64_t w = ((uint64_t)w_high << 32) | w_low;
    uint64_t r = (w >> 7) | (w << (64 - 7));
    return (uint32_t)(r >> 32);
}

static inline uint32_t custom_ROR64L_7(uint32_t w_high, uint32_t w_low) {
    uint64_t w = ((uint64_t)w_high << 32) | w_low;
    uint64_t r = (w >> 7) | (w << (64 - 7));
    return (uint32_t)(r);
}

static inline uint32_t custom_ROR64H_41(uint32_t w_high, uint32_t w_low) {
    uint64_t w = ((uint64_t)w_high << 32) | w_low;
    uint64_t r = (w >> 41) | (w << (64 - 41));
    return (uint32_t)(r >> 32);
}

static inline uint32_t custom_ROR64L_41(uint32_t w_high, uint32_t w_low) {
    uint64_t w = ((uint64_t)w_high << 32) | w_low;
    uint64_t r = (w >> 41) | (w << (64 - 41));
    return (uint32_t)(r);
}

static inline uint32_t custom_OP_ASCON(uint32_t w1, uint32_t w2, uint32_t w3) {
    return w1 ^ (~w2 & w3);
}

static inline uint32_t MULTI_ROR64H_19_28(uint32_t w_high, uint32_t w_low) {
    return w_high ^ custom_ROR64H_19(w_high, w_low) ^ custom_ROR64H_28(w_high, w_low);
}

static inline uint32_t MULTI_ROR64L_19_28(uint32_t w_high, uint32_t w_low) {
    return w_low ^ custom_ROR64L_19(w_high, w_low) ^ custom_ROR64L_28(w_high, w_low);
}

static inline uint32_t MULTI_ROR64H_61_39(uint32_t w_high, uint32_t w_low) {
    return w_high ^ custom_ROR64H_61(w_high, w_low) ^ custom_ROR64H_39(w_high, w_low);
}

static inline uint32_t MULTI_ROR64L_61_39(uint32_t w_high, uint32_t w_low) {
    return w_low ^ custom_ROR64L_61(w_high, w_low) ^ custom_ROR64L_39(w_high, w_low);
}

static inline uint32_t MULTI_ROR64H_1_6(uint32_t w_high, uint32_t w_low) {
    return w_high ^ custom_ROR64H_1(w_high, w_low) ^ custom_ROR64H_6(w_high, w_low);
}

static inline uint32_t MULTI_ROR64L_1_6(uint32_t w_high, uint32_t w_low) {
    return w_low ^ custom_ROR64L_1(w_high, w_low) ^ custom_ROR64L_6(w_high, w_low);
}

static inline uint32_t MULTI_ROR64H_10_17(uint32_t w_high, uint32_t w_low) {
    return w_high ^ custom_ROR64H_10(w_high, w_low) ^ custom_ROR64H_17(w_high, w_low);
}

static inline uint32_t MULTI_ROR64L_10_17(uint32_t w_high, uint32_t w_low) {
    return w_low ^ custom_ROR64L_10(w_high, w_low) ^ custom_ROR64L_17(w_high, w_low);
}

static inline uint32_t MULTI_ROR64H_7_41(uint32_t w_high, uint32_t w_low) {
    return w_high ^ custom_ROR64H_7(w_high, w_low) ^ custom_ROR64H_41(w_high, w_low);
}

static inline uint32_t MULTI_ROR64L_7_41(uint32_t w_high, uint32_t w_low) {
    return w_low ^ custom_ROR64L_7(w_high, w_low) ^ custom_ROR64L_41(w_high, w_low);
}

#else

static inline uint32_t custom_ROR64H_19(uint32_t w_high, uint32_t w_low) {
    uint32_t result;
    asm volatile (
        ".insn r CUSTOM_0, 0, 38, %[rd], %[rs1], %[rs2]\n\t"
        : [rd] "=r" (result)
        : [rs1] "r"(w_high), [rs2] "r"(w_low)
    );
    return result;
}

static inline uint32_t custom_ROR64L_19(uint32_t w_high, uint32_t w_low) {
    uint32_t result;
    asm volatile (
        ".insn r CUSTOM_0, 1, 38, %[rd], %[rs1], %[rs2]\n\t"
        : [rd] "=r" (result)
        : [rs1] "r"(w_high), [rs2] "r"(w_low)
    );
    return result;
}

static inline uint32_t custom_ROR64H_28(uint32_t w_high, uint32_t w_low) {
    uint32_t result;
    asm volatile (
        ".insn r CUSTOM_0, 0, 56, %[rd], %[rs1], %[rs2]\n\t"
        : [rd] "=r" (result)
        : [rs1] "r"(w_high), [rs2] "r"(w_low)
    );
    return result;
}

static inline uint32_t custom_ROR64L_28(uint32_t w_high, uint32_t w_low) {
    uint32_t result;
    asm volatile (
        ".insn r CUSTOM_0, 1, 56, %[rd], %[rs1], %[rs2]\n\t"
        : [rd] "=r" (result)
        : [rs1] "r"(w_high), [rs2] "r"(w_low)
    );
    return result;
}

static inline uint32_t custom_ROR64H_61(uint32_t w_high, uint32_t w_low) {
    uint32_t result;
    asm volatile (
        ".insn r CUSTOM_0, 0, 122, %[rd], %[rs1], %[rs2]\n\t"
        : [rd] "=r" (result)
        : [rs1] "r"(w_high), [rs2] "r"(w_low)
    );
    return result;
}

static inline uint32_t custom_ROR64L_61(uint32_t w_high, uint32_t w_low) {
    uint32_t result;
    asm volatile (
        ".insn r CUSTOM_0, 1, 122, %[rd], %[rs1], %[rs2]\n\t"
        : [rd] "=r" (result)
        : [rs1] "r"(w_high), [rs2] "r"(w_low)
    );
    return result;
}

static inline uint32_t custom_ROR64H_39(uint32_t w_high, uint32_t w_low) {
    uint32_t result;
    asm volatile (
        ".insn r CUSTOM_0, 0, 78, %[rd], %[rs1], %[rs2]\n\t"
        : [rd] "=r" (result)
        : [rs1] "r"(w_high), [rs2] "r"(w_low)
    );
    return result;
}

static inline uint32_t custom_ROR64L_39(uint32_t w_high, uint32_t w_low) {
    uint32_t result;
    asm volatile (
        ".insn r CUSTOM_0, 1, 78, %[rd], %[rs1], %[rs2]\n\t"
        : [rd] "=r" (result)
        : [rs1] "r"(w_high), [rs2] "r"(w_low)
    );
    return result;
}

static inline uint32_t custom_ROR64H_1(uint32_t w_high, uint32_t w_low) {
    uint32_t result;
    asm volatile (
        ".insn r CUSTOM_0, 0, 2, %[rd], %[rs1], %[rs2]\n\t"
        : [rd] "=r" (result)
        : [rs1] "r"(w_high), [rs2] "r"(w_low)
    );
    return result;
}

static inline uint32_t custom_ROR64L_1(uint32_t w_high, uint32_t w_low) {
    uint64_t result;
    asm volatile (
        ".insn r CUSTOM_0, 1, 2, %[rd], %[rs1], %[rs2]\n\t"
        : [rd] "=r" (result)
        : [rs1] "r"(w_high), [rs2] "r"(w_low)
    );
    return result;
}

static inline uint32_t custom_ROR64H_6(uint32_t w_high, uint32_t w_low) {
    uint32_t result;
    asm volatile (
        ".insn r CUSTOM_0, 0, 6, %[rd], %[rs1], %[rs2]\n\t"
        : [rd] "=r" (result)
        : [rs1] "r"(w_high), [rs2] "r"(w_low)
    );
    return result;
}

static inline uint32_t custom_ROR64L_6(uint32_t w_high, uint32_t w_low) {
    uint32_t result;
    asm volatile (
        ".insn r CUSTOM_0, 1, 6, %[rd], %[rs1], %[rs2]\n\t"
        : [rd] "=r" (result)
        : [rs1] "r"(w_high), [rs2] "r"(w_low)
    );
    return result;
}

static inline uint32_t custom_ROR64H_10(uint32_t w_high, uint32_t w_low) {
    uint32_t result;
    asm volatile (
        ".insn r CUSTOM_0, 0, 20, %[rd], %[rs1], %[rs2]\n\t"
        : [rd] "=r" (result)
        : [rs1] "r"(w_high), [rs2] "r"(w_low)
    );
    return result;
}

static inline uint32_t custom_ROR64L_10(uint32_t w_high, uint32_t w_low) {
    uint32_t result;
    asm volatile (
        ".insn r CUSTOM_0, 1, 20, %[rd], %[rs1], %[rs2]\n\t"
        : [rd] "=r" (result)
        : [rs1] "r"(w_high), [rs2] "r"(w_low)
    );
    return result;
}

static inline uint32_t custom_ROR64H_17(uint32_t w_high, uint32_t w_low) {
    uint32_t result;
    asm volatile (
        ".insn r CUSTOM_0, 0, 34, %[rd], %[rs1], %[rs2]\n\t"
        : [rd] "=r" (result)
        : [rs1] "r"(w_high), [rs2] "r"(w_low)
    );
    return result;
}

static inline uint32_t custom_ROR64L_17(uint32_t w_high, uint32_t w_low) {
    uint32_t result;
    asm volatile (
        ".insn r CUSTOM_0, 1, 34, %[rd], %[rs1], %[rs2]\n\t"
        : [rd] "=r" (result)
        : [rs1] "r"(w_high), [rs2] "r"(w_low)
    );
    return result;
}

static inline uint32_t custom_ROR64H_7(uint32_t w_high, uint32_t w_low) {
    uint32_t result;
    asm volatile (
        ".insn r CUSTOM_0, 0, 14, %[rd], %[rs1], %[rs2]\n\t"
        : [rd] "=r" (result)
        : [rs1] "r"(w_high), [rs2] "r"(w_low)
    );
    return result;
}

static inline uint32_t custom_ROR64L_7(uint32_t w_high, uint32_t w_low) {
    uint32_t result;
    asm volatile (
        ".insn r CUSTOM_0, 1, 14, %[rd], %[rs1], %[rs2]\n\t"
        : [rd] "=r" (result)
        : [rs1] "r"(w_high), [rs2] "r"(w_low)
    );
    return result;
}

static inline uint32_t custom_ROR64H_41(uint32_t w_high, uint32_t w_low) {
    uint32_t result;
    asm volatile (
        ".insn r CUSTOM_0, 0, 82, %[rd], %[rs1], %[rs2]\n\t"
        : [rd] "=r" (result)
        : [rs1] "r"(w_high), [rs2] "r"(w_low)
    );
    return result;
}

static inline uint32_t custom_ROR64L_41(uint32_t w_high, uint32_t w_low) {
    uint32_t result;
    asm volatile (
        ".insn r CUSTOM_0, 1, 82, %[rd], %[rs1], %[rs2]\n\t"
        : [rd] "=r" (result)
        : [rs1] "r"(w_high), [rs2] "r"(w_low)
    );
    return result;
}

static inline uint32_t custom_OP_ASCON(uint32_t w1, uint32_t w2, uint32_t w3) {
    uint32_t result;
    asm volatile (
        ".insn r4 CUSTOM_0, 2, 0, %[rd], %[rs1], %[rs2], %[rs3]\n\t"
        : [rd] "=r" (result)
        : [rs1] "r"(w1), [rs2] "r"(w2), [rs3] "r"(w3)
    );
    return result;
}

static inline uint32_t MULTI_ROR64H_19_28(uint32_t w_high, uint32_t w_low) {
    uint32_t result;
        asm volatile (
        ".insn r CUSTOM_0, 4, 0, %[rd], %[rs1], %[rs2]\n\t"
        : [rd] "=r" (result)
        : [rs1] "r"(w_high), [rs2] "r"(w_low)
    );
    return result;
}

static inline uint32_t MULTI_ROR64L_19_28(uint32_t w_high, uint32_t w_low) {
    uint32_t result;
        asm volatile (
        ".insn r CUSTOM_0, 5, 0, %[rd], %[rs1], %[rs2]\n\t"
        : [rd] "=r" (result)
        : [rs1] "r"(w_high), [rs2] "r"(w_low)
    );
    return result;
}

static inline uint32_t MULTI_ROR64H_61_39(uint32_t w_high, uint32_t w_low) {
    uint32_t result;
        asm volatile (
        ".insn r CUSTOM_0, 4, 1, %[rd], %[rs1], %[rs2]\n\t"
        : [rd] "=r" (result)
        : [rs1] "r"(w_high), [rs2] "r"(w_low)
    );
    return result;
}

static inline uint32_t MULTI_ROR64L_61_39(uint32_t w_high, uint32_t w_low) {
    uint32_t result;
        asm volatile (
        ".insn r CUSTOM_0, 5, 1, %[rd], %[rs1], %[rs2]\n\t"
        : [rd] "=r" (result)
        : [rs1] "r"(w_high), [rs2] "r"(w_low)
    );
    return result;
}

static inline uint32_t MULTI_ROR64H_1_6(uint32_t w_high, uint32_t w_low) {
    uint32_t result;
        asm volatile (
        ".insn r CUSTOM_0, 4, 2, %[rd], %[rs1], %[rs2]\n\t"
        : [rd] "=r" (result)
        : [rs1] "r"(w_high), [rs2] "r"(w_low)
    );
    return result;
}

static inline uint32_t MULTI_ROR64L_1_6(uint32_t w_high, uint32_t w_low) {
    uint32_t result;
        asm volatile (
        ".insn r CUSTOM_0, 5, 2, %[rd], %[rs1], %[rs2]\n\t"
        : [rd] "=r" (result)
        : [rs1] "r"(w_high), [rs2] "r"(w_low)
    );
    return result;
}

static inline uint32_t MULTI_ROR64H_10_17(uint32_t w_high, uint32_t w_low) {
    uint32_t result;
        asm volatile (
        ".insn r CUSTOM_0, 4, 3, %[rd], %[rs1], %[rs2]\n\t"
        : [rd] "=r" (result)
        : [rs1] "r"(w_high), [rs2] "r"(w_low)
    );
    return result;
}

static inline uint32_t MULTI_ROR64L_10_17(uint32_t w_high, uint32_t w_low) {
    uint32_t result;
        asm volatile (
        ".insn r CUSTOM_0, 5, 3, %[rd], %[rs1], %[rs2]\n\t"
        : [rd] "=r" (result)
        : [rs1] "r"(w_high), [rs2] "r"(w_low)
    );
    return result;
}

static inline uint32_t MULTI_ROR64H_7_41(uint32_t w_high, uint32_t w_low) {
    uint32_t result;
        asm volatile (
        ".insn r CUSTOM_0, 4, 4, %[rd], %[rs1], %[rs2]\n\t"
        : [rd] "=r" (result)
        : [rs1] "r"(w_high), [rs2] "r"(w_low)
    );
    return result;
}

static inline uint32_t MULTI_ROR64L_7_41(uint32_t w_high, uint32_t w_low) {
        uint32_t result;
        asm volatile (
        ".insn r CUSTOM_0, 5, 4, %[rd], %[rs1], %[rs2]\n\t"
        : [rd] "=r" (result)
        : [rs1] "r"(w_high), [rs2] "r"(w_low)
    );
    return result;
}


#endif // NO_RISCV_ASM

#endif //ASM_H
