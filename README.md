
# RISCV-Crypto-Benchmark

**RISCV-Crypto-Benchmark** is a project designed to measure the performance of some symmetric-key cryptographic algorithms (AES,ChaCha20 and ASCON) on **RISC-V THALES SOFTCORE CV32A6** architecture (with and without custom arithemtic instructions implemented on a CVXIF coprocessor) emulated on **ZYBO Z7-20** board. It enables the evaluation and comparison of differents cryptographics algorithms in terms of numbers of instructions and cycles used. 

It is based on the [**THALES CVA6 SOFTCORE CONTEST**](https://github.com/ThalesGroup/cva6-softcore-contest/blob/cv32a6_contest_24_25) toolchain and my own version of the CVA6 softcore, implementing a custom CVXIF coprocessor : [cva6_crypto](https://github.com/TristanBALDIT/cva6_crypto).

In addition, it contains some plotting python scripts already loaded with some of my measured datas.
The resulting graphs are in the **/results** folder.

## Getting started


