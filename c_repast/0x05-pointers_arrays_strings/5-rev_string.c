#include "main.h"

void rev_string(char *s)
{
    char *recorre = s, prov = 0;
    int l = 0, n = 0, i = 0;

    l = _strlen(recorre);
    n = l / 2;
    l--;
    while (n--)
    {
        prov = s[i];
        s[i] = s[l];
        s[l] = prov;
        l--;
        i++;
    }
}
