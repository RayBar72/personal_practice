#include "main.h"

void print_chessboard(char (*a)[8])
{
    int i = 0, j = 0;

    for (i = 0; i < 8; i ++)
    {
        for (j = 0; j < 8; j ++)
        {
            if (i <= 1 || i >= 6)
            {
                putchar(a[i][j]);
            }
            if (j == 7)
            {
                putchar('\n');
            }
        }
    }
}