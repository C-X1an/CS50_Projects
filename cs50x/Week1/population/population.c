#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // TODO: Prompt for start size
    int start;
    do
    {
        start = get_int("What is the start size?\n ");
    }
    while (start < 9);

    // TODO: Prompt for end size
    int end;
    do
    {
        end = get_int("What is the end size?\n ");
    }
    while (end < start);
    // TODO: Calculate number of years until we reach threshold
    int n = 0;
    while (end > start)
    {
        start = start + (start/3) - (start/4);
        n++;
    }

    // TODO: Print number of years
    printf("Years: %i\n ", n);
}
