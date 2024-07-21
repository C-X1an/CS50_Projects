// Write a function to replace vowels with numbers
// Get practice with strings
// Get practice with command line
// Get practice with switch
#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

char replace(string word, int i);

int main(int argc, string argv[])
{
    string word;
    if (argv[1] == NULL)
    {
        printf("Usage: ./no-vowels word\n");
        return 1;
    }
    else
    {
        word = argv[1];
    }

    for (int i = 0; i < strlen(word); i++)
    {
        if (word[i] == 'a')
        {
            word[i] = replace(word, i);
            printf("%c", word[i]);
        }
        else if (word[i] == 'e')
        {
            word[i] = replace(word, i);
            printf("%c", word[i]);
        }
        else if (word[i] == 'i')
        {
            word[i] = replace(word, i);
            printf("%c", word[i]);
        }
        else if (word[i] == 'o')
        {
            word[i] = replace(word, i);
            printf("%c", word[i]);
        }
        else
        {
            printf("%c", word[i]);
        }
    }
    printf("\n");
    return 0;
}

char replace(string word, int i)
{
    if (word[i] == 'a')
    {
        word[i] = '6';
        return word[i];
    }
    else if (word[i] == 'e')
    {
        word[i] = '3';
        return word[i];
    }
    else if (word[i] == 'i')
    {
        word[i] = '1';
        return word[i];
    }
    else
    {
        word[i] = '0';
        return word[i];
    }
}
