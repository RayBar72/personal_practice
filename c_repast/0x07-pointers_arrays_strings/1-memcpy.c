#include "main.h"

char *_memcpy(char *dest, char *src, unsigned int n)
{
    char *mov = dest;

    while (n --)
    {
        *mov = *src;
        mov ++;
        src ++;
    }
    return (dest);
}
