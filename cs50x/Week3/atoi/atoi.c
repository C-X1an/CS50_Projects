#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int convert(string input, int n);

int main(void)
{
    string input = get_string("Enter a positive integer: ");

    for (int i = 0, n = strlen(input); i < n; i++)
    {
        if (!isdigit(input[i]))
        {
            printf("Invalid Input!\n");
            return 1;
        }
    }

     //Convert string to int
    printf("%i\n", convert(input, strlen(input) - 1));
}

int convert(string input, int n)
{
    // TODO
    while(n >= 0)
    {
        input[n] = input[n] - '0';
        return input[n] + 10 * convert(input, n - 1);
    }
    return 0;





    //while(n >= 0)
    //{
        //return (10 * convert(input, n - 1) + (input[n] - '0'));
    //}
    //return 0;

}
