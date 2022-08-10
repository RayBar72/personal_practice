#include "main.h"

char *_strcpy(char *dest, char *src)
{
    char *mov = dest;

    while (*src)
    {
        *mov = *src;
        mov ++;
        src ++;
    }
    *mov = '\0';
    return (dest);
}
