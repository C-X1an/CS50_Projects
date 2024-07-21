#include <cs50.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "wav.h"

int check_format(WAVHEADER header);
int get_block_size(WAVHEADER header);

int main(int argc, char *argv[])
{
    // Ensure proper usage
    // TODO #1
    if (argc != 3)
    {
        printf("./reverse input.wav output.wav\n");
        return 1;
    }

    // Open input file for reading
    // TODO #2
    if (argv[1] == NULL)
    {
        printf("Input is not a WAV file.\n");
        return 1;
    }
    else if (strcmp(argv[1], "input.wav") != 0)
    {
        printf("Input is not a WAV file.\n");
        return 1;
    }
    FILE *input = fopen(argv[1], "r");
    // Read header
    // TODO #3
    WAVHEADER copy;
    fread(&copy, sizeof(uint8_t), 44, input);

    // Use check_format to ensure WAV format
    // TODO #4

    // Open output file for writing
    // TODO #5
    FILE *output = fopen(argv[2], "w");
    if (argv[2] == NULL)
    {
        return 1;
    }

    // Write header to file
    // TODO #6

    fwrite(&copy, sizeof(uint8_t), 44, output);

    // Use get_block_size to calculate size of block
    // TODO #7
    int size_block = get_block_size(copy);
    printf("%i", size_block);

    // Write reversed audio to file
    // TODO #8
    uint32_t samples[88201];
    long i = 0;
    while (fread(&samples[i], 4, 1, input) != 0)
    {
        i++;
    }

    for (int j = i - 1; j >= 0; j--)
    {
        fwrite(&samples[j], 4, 1, output);
    }

    fclose(input);
    fclose(output);
}

int check_format(WAVHEADER header)
{
    // TODO #4
    string wave = "WAVE";
    int check = 0;
    for (int i = 0; i < 4; i++)
    {
        if ((int) wave[i] == header.format[i])
        {
            check++;
        }
    }
    if (check == 4)
    {
        return 0;
    }
    else
    {
        printf("Input is not a WAV file.\n");
        return 1;
    }
    return 1;
}

int get_block_size(WAVHEADER header)
{
    // TODO #7
    return (header.numChannels * (header.bitsPerSample / 8));
}
