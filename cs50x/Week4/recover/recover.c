#include <cs50.h>
#include <ctype.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("./recover IMAGE\n");
        return 1;
    }
    if (strcmp(argv[1], "card.raw") != 0)
    {
        return 1;
    }
    FILE *input = fopen(argv[1], "r");

    uint8_t copy[512];
    char *jpg = malloc(8);

    int x = 0;
    FILE *output;
    while (fread(&copy, 512, 1, input) != 0)
    {
        if (copy[0] == 0xff && copy[1] == 0xd8 && copy[2] == 0xff && ((copy[3] & 0xf0) == 0xe0))
        {
            sprintf(jpg, "%03i.jpg", x);
            if (x > 0)
            {
                fclose(output);
            }
            output = fopen(jpg, "w");
            fwrite(&copy, 512, 1, output);
            x++;
        }
        else if (x > 0)
        {
            fwrite(&copy, 512, 1, output);
        }
    }
    free(jpg);
    fclose(input);
    fclose(output);
    return 0;
}
