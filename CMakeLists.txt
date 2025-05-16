cmake_minimum_required(VERSION 3.29)
project(RISCV_Crypto_Benchmark C)

set(CMAKE_C_STANDARD 11)

add_executable(RISCV_Crypto_Benchmark main.c
        aes/aes.c
        aes/aes.h
        chacha/chacha.c
        chacha/chacha.h
        loader.c
        loader.h
        aes/aes.c
        chacha/poly1305.c
        chacha/poly1305.h
        monocypher.c
        monocypher.h
        ascon/ascon.c
        ascon/ascon.h
        "opcodes test/ror64.c"
        ascon/asm.h)
