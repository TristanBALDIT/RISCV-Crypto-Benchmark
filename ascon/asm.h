//
// Created by trist on 16/05/2025.
//

#ifndef ASM_H
#define ASM_H

#include <stdint.h>

inline uint32_t custom_ROR64H_19(uint32_t w_high, uint32_t w_low);
inline uint32_t custom_ROR64L_19(uint32_t w_high, uint32_t w_low);
inline uint32_t custom_ROR64H_28(uint32_t w_high, uint32_t w_low);
inline uint32_t custom_ROR64L_28(uint32_t w_high, uint32_t w_low);
inline uint32_t custom_ROR64H_61(uint32_t w_high, uint32_t w_low);
inline uint32_t custom_ROR64L_61(uint32_t w_high, uint32_t w_low);
inline uint32_t custom_ROR64H_39(uint32_t w_high, uint32_t w_low);
inline uint32_t custom_ROR64L_39(uint32_t w_high, uint32_t w_low);
inline uint32_t custom_ROR64H_1(uint32_t w_high, uint32_t w_low);
inline uint32_t custom_ROR64L_1(uint32_t w_high, uint32_t w_low);
inline uint32_t custom_ROR64H_6(uint32_t w_high, uint32_t w_low);
inline uint32_t custom_ROR64L_6(uint32_t w_high, uint32_t w_low);
inline uint32_t custom_ROR64H_10(uint32_t w_high, uint32_t w_low);
inline uint32_t custom_ROR64L_10(uint32_t w_high, uint32_t w_low);
inline uint32_t custom_ROR64H_17(uint32_t w_high, uint32_t w_low);
inline uint32_t custom_ROR64L_17(uint32_t w_high, uint32_t w_low);
inline uint32_t custom_ROR64H_7(uint32_t w_high, uint32_t w_low);
inline uint32_t custom_ROR64L_7(uint32_t w_high, uint32_t w_low);
inline uint32_t custom_ROR64H_41(uint32_t w_high, uint32_t w_low);
inline uint32_t custom_ROR64L_41(uint32_t w_high, uint32_t w_low);

#define CUSTOM_ROR64H_19(result, w_high, w_low)                     \
    asm volatile (                                                  \
        ".insn r CUSTOM_0, 0, 38, %[rd], %[rs1], %[rs2]\n\t"        \
        : [rd] "=r" (result)                                        \
        : [rs1] "r"(w_high), [rs2] "r"(w_low)                       \
    )

#define CUSTOM_ROR64L_19(result, w_high, w_low)                     \
    asm volatile (                                                  \
        ".insn r CUSTOM_0, 1, 38, %[rd], %[rs1], %[rs2]\n\t"        \
        : [rd] "=r" (result)                                        \
        : [rs1] "r"(w_high), [rs2] "r"(w_low)                       \
    )

#define CUSTOM_ROR64H_28(result, w_high, w_low)                     \
    asm volatile (                                                  \
        ".insn r CUSTOM_0, 0, 56, %[rd], %[rs1], %[rs2]\n\t"        \
        : [rd] "=r" (result)                                        \
        : [rs1] "r"(w_high), [rs2] "r"(w_low)                       \
    )

#define CUSTOM_ROR64L_28(result, w_high, w_low)                     \
    asm volatile (                                                  \
        ".insn r CUSTOM_0, 1, 56, %[rd], %[rs1], %[rs2]\n\t"        \
        : [rd] "=r" (result)                                        \
        : [rs1] "r"(w_high), [rs2] "r"(w_low)                       \
)

#define CUSTOM_ROR64H_61(result, w_high, w_low)                     \
    asm volatile (                                                  \
        ".insn r CUSTOM_0, 0, 122, %[rd], %[rs1], %[rs2]\n\t"       \
        : [rd] "=r" (result)                                        \
        : [rs1] "r"(w_high), [rs2] "r"(w_low)                       \
)

#define CUSTOM_ROR64L_61(result, w_high, w_low)                     \
    asm volatile (                                                  \
        ".insn r CUSTOM_0, 1, 122, %[rd], %[rs1], %[rs2]\n\t"       \
        : [rd] "=r" (result)                                        \
        : [rs1] "r"(w_high), [rs2] "r"(w_low)                       \
    )

#define CUSTOM_ROR64H_39(result, w_high, w_low)                     \
    asm volatile (                                                  \
        ".insn r CUSTOM_0, 0, 78, %[rd], %[rs1], %[rs2]\n\t"        \
        : [rd] "=r" (result)                                        \
        : [rs1] "r"(w_high), [rs2] "r"(w_low)                       \
    )

#define CUSTOM_ROR64L_39(result, w_high, w_low)                     \
    asm volatile (                                                  \
        ".insn r CUSTOM_0, 1, 78, %[rd], %[rs1], %[rs2]\n\t"        \
        : [rd] "=r" (result)                                        \
        : [rs1] "r"(w_high), [rs2] "r"(w_low)                       \
    )

#define CUSTOM_ROR64H_1(result, w_high, w_low)                      \
    asm volatile (                                                  \
        ".insn r CUSTOM_0, 0, 2, %[rd], %[rs1], %[rs2]\n\t"         \
        : [rd] "=r" (result)                                        \
        : [rs1] "r"(w_high), [rs2] "r"(w_low)                       \
    )

#define CUSTOM_ROR64L_1(result, w_high, w_low)                      \
    asm volatile (                                                  \
        ".insn r CUSTOM_0, 1, 2, %[rd], %[rs1], %[rs2]\n\t"         \
        : [rd] "=r" (result)                                        \
        : [rs1] "r"(w_high), [rs2] "r"(w_low)                       \
    )

#define CUSTOM_ROR64H_6(result, w_high, w_low)                      \
asm volatile (                                                      \
        ".insn r CUSTOM_0, 0, 12, %[rd], %[rs1], %[rs2]\n\t"        \
        : [rd] "=r" (result)                                        \
        : [rs1] "r"(w_high), [rs2] "r"(w_low)                       \
    )

#define CUSTOM_ROR64L_6(result, w_high, w_low)                      \
    asm volatile (                                                  \
        ".insn r CUSTOM_0, 1, 12, %[rd], %[rs1], %[rs2]\n\t"        \
        : [rd] "=r" (result)                                        \
        : [rs1] "r"(w_high), [rs2] "r"(w_low)                       \
    )

#define CUSTOM_ROR64H_10(result, w_high, w_low)                     \
    asm volatile (                                                  \
        ".insn r CUSTOM_0, 0, 20, %[rd], %[rs1], %[rs2]\n\t"        \
        : [rd] "=r" (result)                                        \
        : [rs1] "r"(w_high), [rs2] "r"(w_low)                       \
    )

#define CUSTOM_ROR64L_10(result, w_high, w_low)                     \
    asm volatile (                                                  \
        ".insn r CUSTOM_0, 1, 20, %[rd], %[rs1], %[rs2]\n\t"        \
        : [rd] "=r" (result)                                        \
        : [rs1] "r"(w_high), [rs2] "r"(w_low)                       \
    )

#define CUSTOM_ROR64H_17(result, w_high, w_low)                     \
    asm volatile (                                                  \
        ".insn r CUSTOM_0, 0, 34, %[rd], %[rs1], %[rs2]\n\t"        \
        : [rd] "=r" (result)                                        \
        : [rs1] "r"(w_high), [rs2] "r"(w_low)                       \
    )

#define CUSTOM_ROR64L_17(result, w_high, w_low)                     \
    asm volatile (                                                  \
        ".insn r CUSTOM_0, 1, 34, %[rd], %[rs1], %[rs2]\n\t"        \
        : [rd] "=r" (result)                                        \
        : [rs1] "r"(w_high), [rs2] "r"(w_low)                       \
    )

#define CUSTOM_ROR64H_7(result, w_high, w_low)                      \
    asm volatile (                                                  \
        ".insn r CUSTOM_0, 0, 14, %[rd], %[rs1], %[rs2]\n\t"        \
        : [rd] "=r" (result)                                        \
        : [rs1] "r"(w_high), [rs2] "r"(w_low)                       \
    )

#define CUSTOM_ROR64L_7(result, w_high, w_low)                      \
    asm volatile (                                                  \
        ".insn r CUSTOM_0, 1, 14, %[rd], %[rs1], %[rs2]\n\t"        \
        : [rd] "=r" (result)                                        \
        : [rs1] "r"(w_high), [rs2] "r"(w_low)                       \
    )

#define CUSTOM_ROR64H_41(result, w_high, w_low)                     \
    asm volatile (                                                  \
        ".insn r CUSTOM_0, 0, 82, %[rd], %[rs1], %[rs2]\n\t"        \
        : [rd] "=r" (result)                                        \
        : [rs1] "r"(w_high), [rs2] "r"(w_low)                       \
    )

#define CUSTOM_ROR64L_41(result, w_high, w_low)                     \
    asm volatile (                                                  \
        ".insn r CUSTOM_0, 1, 82, %[rd], %[rs1], %[rs2]\n\t"        \
        : [rd] "=r" (result)                                        \
        : [rs1] "r"(w_high), [rs2] "r"(w_low)                       \
    )
#endif //ASM_H
