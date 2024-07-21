#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // prompt height(1-8)
    int height = get_int("Height: ");
    while (height < 1)
    {
        height = get_int("Height: ");
    }
    while (height > 8)
    {
        height = get_int("Height: ");
    }

    // loop (increase by 1, print one more # code == height +1, while code > height, print #, once code < height, \n
    for (int i = 0; i < height; i++)
    {
        int k = 1;
        while (k < (height - i))
        {
            printf(" ");
            k++;
        }
        for (int j = (i + 1); j > 0; j--)
        {
            printf("#");
        }
        printf("\n");
    }
}
