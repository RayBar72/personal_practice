#!/usr/bin/env python3
'''Modulus that creates the files for the exercise'''



lista = [
    '0-reset_to_98.c',
    '1-swap.c',
    '2-strlen.c',
    '3-puts.c',
    '4-print_rev.c',
    '5-rev_string.c',
    '6-puts2.c',
    '7-puts_half.c',
    '8-print_array.c',
    '9-strcpy.c',
    '100-atoi.c'
    ]

for i in range(10):
    lista.append(str(i) + '-main.c')
lista.append('100-main.c')

for x in lista:
    with open(x, 'w') as f:
        pass
