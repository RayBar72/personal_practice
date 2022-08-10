#include "main.h"

void puts_half(char *str)
{
    int l = 0, n = 0;
    char *s = str;

    l = _strlen(s);
    n = (l - 1) / 2;
    l = n + 1;
    n ++;
    while (n --)
    {
        putchar(str[l]);
        l ++;
    }
    putchar('\n');
}
