#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // ask for height(1-8)
    int height = get_int("What is the height: ");
    while (height < 1)
    {
        height = get_int("What is the height: ");
    }
    while (height > 8)
    {
        height = get_int("What is the height: ");
    }

    // print left-aligned accord. height
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
        printf("  ");
        for (int y = (i + 1); y > 0; y--)
        {
            printf("#");
        }
        printf("\n");
    }
}
