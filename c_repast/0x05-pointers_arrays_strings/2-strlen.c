#include "main.h"

int _strlen(char *s)
{
    char *m = s;
    int res = 0;

    while (*m)
    {
        m++;
        res++;
    }
    return res;
}