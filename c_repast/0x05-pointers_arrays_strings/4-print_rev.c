#include "main.h"

void print_rev(char *s)
{
    char *sr = s;
    int i = 0;

    while (*sr)
    {
        sr++;
        i++;
    }

    while (i--)
    {
        putchar(s[i]);
    }
    putchar('\n');
}
