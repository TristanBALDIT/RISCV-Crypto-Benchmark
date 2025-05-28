
# RISCV-Crypto-Benchmark

**RISCV-Crypto-Benchmark** is a project designed to measure the performance of some symmetric-key cryptographic algorithms (AES,ChaCha20 and ASCON) on the [**RISC-V OPENHW GROUP CV32A6 SOFTCORE**](https://github.com/openhwgroup/cva6) architecture (with and without custom arithmetic instructions implemented on a CVXIF coprocessor) emulated on **ZYBO Z7-20** board. It enables the evaluation and comparison of differents cryptographics algorithms in terms of numbers of instructions and cycles used. 

It is based on the [**THALES CVA6 SOFTCORE CONTEST**](https://github.com/ThalesGroup/cva6-softcore-contest/blob/cv32a6_contest_24_25) toolchain and my own version of the CVA6 softcore, implementing a custom CVXIF coprocessor : [cva6_crypto](https://github.com/TristanBALDIT/cva6_crypto).

In addition, it contains some plotting python scripts already loaded with some of my measured datas.
The resulting graphs are in the **/results** folder.

## Getting started

Checkout my own cva6 repository and initialize all submodules:
```
$ git clone https://github.com/TristanBALDIT/cva6_crypto
$ git submodule update --init --recursive
```

Then checkout the Thales softcore contest (to get the SW toolchain)
```
$ git clone https://github.com/ThalesGroup/cva6-softcore-contest/cv32a6_contest_24_25
```

Copy the  **/sw** and the Dockerfile to your clone of cva6_crypto

You can now follow the guide in the [THALES CVA6 SOFTCORE CONTEST](https://github.com/ThalesGroup/cva6-softcore-contest/blob/cv32a6_contest_24_25) to setup the whole toolchain. 
( /!\ Do it in the **cva6_crypto** clone and not the softcore contest one)



