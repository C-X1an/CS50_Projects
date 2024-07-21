#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, string argv[])
{
    int key = 0;
    if (argv[1] == NULL)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
    else
    {
        key = atoi(argv[1]);
    }
    for (int x = 0; x < strlen(argv[1]); x++)
    {

        if (argv[1][x] < 0)
        {
            printf("Usage: ./caesar key\n");
            return 1;
        }
        else if (argv[1][x] > '9')
        {
            printf("Usage: ./caesar key\n");
            return 1;
        }
    }
    if (argc > 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
    else if (atoi(argv[1]) > 26)
    {
        key = atoi(argv[1]) % 26;
    }
    else
    {
        key = atoi(argv[1]);
    }

    string plaintext = get_string("plaintext: ");

    printf("ciphertext: ");

    for (int i = 0; i < strlen(plaintext); i++)
    {
        if (plaintext[i] < 'A')
        {
            printf("%c", plaintext[i]);
        }
        else
        {
            if ('z' - plaintext[i] < key)
            {
                plaintext[i] = plaintext[i] + key - 26;
            }
            else
            {
                plaintext[i] = plaintext[i] + key;
            }
            printf("%c", plaintext[i]);
        }
    }
    printf("\n");
    return 0;
}
