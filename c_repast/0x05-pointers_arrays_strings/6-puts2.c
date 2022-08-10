#include "main.h"

void puts2(char *str)
{
    int i = 0;

    while (*str)
    {
        if (i % 2 == 0)
            putchar(*str);
        i++;
        str++;
    }
    putchar('\n');
}
