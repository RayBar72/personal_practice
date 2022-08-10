#include "main.h"

void _puts(char *str)
{

    while (*str)
    {
        putchar(*str);
        str++;
    }
    putchar('\n');
}
