#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

const int BITS_IN_BYTE = 8;

void print_bulb(int bit);

int main(void)
{
    // TODO
    string message = get_string("Message: ");

    const int y = strlen(message);

    for (int k = 0; k < y; k++)
    {
        for (int j = 0; j < BITS_IN_BYTE; j++)
        {
            int x = 128 / pow(2, j);

            if ((int) message[k] > x - 1)
            {
                print_bulb(1);
                message[k] = message[k] - x;
            }
            else
            {
                print_bulb(0);
            }
        }
        printf("\n");
    }
}

void print_bulb(int bit)
{
    if (bit == 0)
    {
        // Dark emoji
        printf("\U000026AB");
    }
    else if (bit == 1)
    {
        // Light emoji
        printf("\U0001F7E1");
    }
}
