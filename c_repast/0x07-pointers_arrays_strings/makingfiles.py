#!/usr/bin/env python3
'''Module that creates the files for the project'''


lista = [
    '0-memset.c',
    '1-memcpy.c',
    '2-strchr.c',
    '3-strspn.c',
    '4-strpbrk.c',
    '5-strstr.c',
    '7-print_chessboard.c',
    '8-print_diagsums.c',
    '100-set_string.c',
    '100-main.c',
    'main.h'
    ]

for i in range(9):
    lista.append(str(i) + '-main.c')

for x in lista:
    with open(x, 'w') as f:
        pass
