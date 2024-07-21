#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

int main(int argc, string argv[])
{
    if (argv[1] == NULL)
    {
        printf("Usage: ./substitution key\n");
        return 1;
    }
    for (int k = 0; k < strlen(argv[1]); k++)
    {
        if (argv[1][k] < 'A')
        {
            printf("Usage: ./substitution key\n");
            return 1;
        }
        else if (argv[1][k] > 'Z' && argv[1][k] < 'a')
        {
            printf("Usage: ./substitution key\n");
            return 1;
        }
    }
    if (strlen(argv[1]) < 26)
    {
        printf("Key must contain 26 characters.\n");
        return 1;
    }
    else if (argv[2] != NULL)
    {
        printf("Usage: ./substitution key\n");
        return 1;
    }
    for (int x = 0; x < strlen(argv[1]); x++)
    {
        for (int y = x + 1; y < strlen(argv[1]); y++)
        {
            if (argv[1][x] == argv[1][y])
            {
                printf("Key must not contain repeated characters.\n");
                return 1;
            }
        }
    }

    string plaintext = get_string("plaintext: ");

    printf("ciphertext: ");
    for (int j = 0; j < strlen(plaintext); j++)
    {
        if (islower(plaintext[j]))
        {
            int w = plaintext[j] - 'a';
            printf("%c", tolower(argv[1][w]));
        }
        else if (plaintext[j] == ' ')
        {
            printf(" ");
        }
        else if (plaintext[j] < 'A')
        {
            printf("%c", plaintext[j]);
        }
        else
        {
            int q = plaintext[j] - 'A';
            printf("%c", toupper(argv[1][q]));
        }
    }
    printf("\n");
}
