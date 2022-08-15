#include "main.h"

int record_x(int *b, int size, int pos)
{
    int i = 0, x = 0;

    for (i = 0; i < size; i++)
    {
        if (pos == i)
        {
            printf("%d", x);
            x += b[i];
        }
    }
    return (x);
}

int record_y(int *b, int size, int pos)
{
    int i = 0, y = 0;

    for (i = 0; i < size; i++)
    {
        if (size - pos == i)
        {
            y += b[i];
        }
    }
    return (y);
}

void print_diagsums(int *a, int size)
{
    int i = 0, y = 0, x = 0;

    for (i = 0; i < size; i ++)
    {
        x += record_x(a, size, i);
        y += record_y(a, size, i);
        a ++;
    }
    printf("%d, %d\n", x, y);
}