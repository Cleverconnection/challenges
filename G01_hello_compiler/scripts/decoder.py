#!/usr/bin/env python3
"""Decodificador simples para o desafio G01 — Hello, Compiler."""

KEY = b"HOP"
FLAG_XOR = [
    11, 27, 22, 51, 40, 34, 41, 44, 53, 23,
    55, 63, 58, 16, 61, 41, 59, 53, 37, 46,
    36, 33, 44, 49, 53,
]


def decode() -> str:
    decoded = bytes(
        value ^ KEY[index % len(KEY)]
        for index, value in enumerate(FLAG_XOR)
    )
    return decoded.decode()


if __name__ == "__main__":
    print(decode())
