#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // ask for number(long)
    long number = get_long("Number: ");

    // find 2nd-last digit using (/10, %10)
    int second_last_digit = (number / 10) % 10;
    int sum_products_second = ((second_last_digit * 2) % 10);
    if (second_last_digit > 4)
    {
        sum_products_second++;
    }

    int fourth_last_digit = (number / 1000) % 10;
    int sum_products_fourth = ((fourth_last_digit * 2) % 10);
    if (fourth_last_digit > 4)
    {
        sum_products_fourth++;
    }

    int sixth_last_digit = (number / 100000) % 10;
    int sum_products_sixth = ((sixth_last_digit * 2) % 10);
    if (sixth_last_digit > 4)
    {
        sum_products_sixth++;
    }

    int eighth_last_digit = (number / 10000000) % 10;
    int sum_products_eighth = ((eighth_last_digit * 2) % 10);
    if (eighth_last_digit > 4)
    {
        sum_products_eighth++;
    }

    int tenth_last_digit = (number / 1000000000) % 10;
    int sum_products_tenth = ((tenth_last_digit * 2) % 10);
    if (tenth_last_digit > 4)
    {
        sum_products_tenth++;
    }

    int twelth_last_digit = (number / 100000000000) % 10;
    int sum_products_twelth = ((twelth_last_digit * 2) % 10);
    if(twelth_last_digit > 4)
    {
        sum_products_twelth++;
    }

    int fourteenth_last_digit = (number / 10000000000000) % 10;
    int sum_products_fourteenth = ((fourteenth_last_digit * 2) % 10);
    if(fourteenth_last_digit > 4)
    {
        sum_products_fourteenth++;
    }

    int sixteenth_last_digit = (number / 1000000000000000) % 10;
    int sum_products_sixteenth = ((sixteenth_last_digit * 2) % 10);
    if(sixteenth_last_digit > 4)
    {
        sum_products_sixteenth++;
    }

    int sum_multiplied_digits = (sum_products_sixteenth + sum_products_fourteenth + sum_products_twelth + sum_products_tenth + sum_products_eighth + sum_products_sixth + sum_products_fourth + sum_products_second);

    int last_digit = (number % 10);

    int third_last_digit = (number / 100) % 10;

    int fifth_last_digit = (number / 10000) % 10;

    int seventh_last_digit = (number / 1000000) % 10;

    int ninth_last_digit = (number / 100000000) % 10;

    int eleventh_last_digit = (number / 10000000000) % 10;

    int thirteenth_last_digit = (number / 1000000000000) % 10;

    int fiftheenth_last_digit = (number / 100000000000000) % 10;

    int sum_odd_digits = last_digit + third_last_digit + fifth_last_digit + seventh_last_digit + ninth_last_digit + eleventh_last_digit + thirteenth_last_digit + fiftheenth_last_digit;

    int sum_digits = sum_multiplied_digits + sum_odd_digits;

    int verify = (sum_digits % 10);

    if(verify == 0)
    {
        if(sixteenth_last_digit == 5)
        {
            if(fiftheenth_last_digit < 6)
            {
                printf("MASTERCARD\n");
            }
            else
            {
                printf("INVALID\n");
            }

        }
        else if(fiftheenth_last_digit == 3)
        {
            if(fourteenth_last_digit == 4)
            {
                printf("AMEX\n");
            }
            if(fourteenth_last_digit == 7)
            {
                printf("AMEX\n");
            }
            else
            {
                printf("INVALID\n");
            }

        }
        else if(sixteenth_last_digit == 4)
        {
            printf("VISA\n");
        }
        else if(thirteenth_last_digit == 4)
        {
            printf("VISA\n");
        }
        else
        {
            printf("INVALID\n");
        }
    }
    else
    {
        printf("INVALID\n");
    }
}
