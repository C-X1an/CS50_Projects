// Check that a password has at least one lowercase letter, uppercase letter, number and symbol
// Practice iterating through a string
// Practice using the ctype library

#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

bool valid(string password);

int main(void)
{
    string password = get_string("Enter your password: ");
    if (valid(password))
    {
        printf("Your password is valid!\n");
    }
    else
    {
        printf("Your password needs at least one uppercase letter, lowercase letter, number and symbol\n");
    }
}

// TODO: Complete the Boolean function below
bool valid(string password)
{
    int cat[4];
    for (int i = 0; i < strlen(password); i++)
    {
        if ('@' < password[i] && password[i] < '[')
        {
            cat[0]++;
        }
        else if (password[i] > '`' && password[i] < '{')
        {
            cat[1]++;
        }
        else if (password[i] > '/' && password[i] < ':')
        {
            cat[2]++;
        }
        else
        {
            cat[3]++;
        }
    }
    int score = 0;
    for (int j = 0; j < 4; j++)
    {
        if (cat[j] > 0)
        {
            score++;
        }
        else
        {
            score = score + 0;
        }
    }
    if (score == 4)
    {
        return true;
    }
    else
    {
        return false;
    }
}
