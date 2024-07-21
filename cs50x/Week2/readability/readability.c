#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

int count_letters(string text);
int count_words(string text);
int count_sentence(string text);

int main(void)
{
    string text = get_string("Text: ");

    for (int y = 0; y < strlen(text); y++)
    {
        if (isupper(text[y]))
        {
            text[y] = tolower(text[y]);
        }
        else
        {
            text[y] = text[y] + 0;
        }
    }

    int letters = count_letters(text);

    int words = count_words(text);

    int sentence = count_sentence(text);

    float L = (((float) letters / (float) words) * 100);

    float S = (((float) sentence / (float) words) * 100);

    float q = 0.0588 * L - 0.296 * S - 15.8;

    int index = q;

    int round_up = ((int) (q * 10) % 10);

    if (round_up > 4)
    {
        index++;
    }
    else
    {
        index = index + 0;
    }

    if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (index > 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n", index);
    }
}

int count_letters(string text)
{
    int x = 0;
    for (int i = 0; i < strlen(text); i++)
    {
        if ('`' < text[i] && text[i] < '}')
        {
            x++;
        }
        else
        {
            x = x + 0;
        }
    }
    return x;
}

int count_words(string text)
{
    int k = 0;
    for (int j = 0; j < strlen(text); j++)
    {
        if (text[j] == ' ')
        {
            k++;
        }
        else
        {
            k = k + 0;
        }
    }
    return k + 1;
}

int count_sentence(string text)
{
    int z = 0;
    for (int m = 0; m < strlen(text); m++)
    {
        if (text[m] == '.')
        {
            z++;
        }
        else if (text[m] == '!')
        {
            z++;
        }
        else if (text[m] == '?')
        {
            z++;
        }
        else
        {
            z = z + 0;
        }
    }
    return z;
}
