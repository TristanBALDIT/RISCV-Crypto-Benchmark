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
        aes/aes.c)
