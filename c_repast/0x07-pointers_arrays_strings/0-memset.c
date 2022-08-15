#include "main.h"

char *_memset(char *s, char b, unsigned int n)
{
    char *reco = s;

    while (n --)
    {
        *reco = b;
        reco ++;
    }
    return s;
}