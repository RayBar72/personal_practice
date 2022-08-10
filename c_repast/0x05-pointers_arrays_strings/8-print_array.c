#include "main.h"

void print_array(int *a, int n)
{
    while (n --)
    {
        printf("%d", *a);
        a ++;
        if (n != 0)
            printf(", ");
    }
    putchar('\n');
}