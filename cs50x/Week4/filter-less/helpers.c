#include "helpers.h"
#include <cs50.h>
#include <stdio.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    float shade;
    for (int i = 0; i < width; i++)
    {
        for (int j = 0; j < height; j++)
        {
            shade = (image[j][i].rgbtBlue + image[j][i].rgbtGreen + image[j][i].rgbtRed) / 3.00;
            if ((int) (shade * 10) % 10 > 5)
            {
                image[j][i].rgbtBlue = shade + 1;
                image[j][i].rgbtRed = shade + 1;
                image[j][i].rgbtGreen = shade + 1;
            }
            else
            {
                image[j][i].rgbtBlue = shade;
                image[j][i].rgbtRed = shade;
                image[j][i].rgbtGreen = shade;
            }
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    BYTE originalGreen;
    BYTE originalRed;
    BYTE originalBlue;
    for (int i = 0; i < width; i++)
    {
        for (int j = 0; j < height; j++)
        {
            originalBlue = image[j][i].rgbtBlue;
            originalRed = image[j][i].rgbtRed;
            originalGreen = image[j][i].rgbtGreen;
            if ((int) ((.393 * originalRed + .769 * originalGreen + .189 * originalBlue) * 10) % 10 > 4)
            {
                image[j][i].rgbtRed = .393 * originalRed + .769 * originalGreen + .189 * originalBlue + 1;
            }
            else
            {
                image[j][i].rgbtRed = .393 * originalRed + .769 * originalGreen + .189 * originalBlue;
            }
            if (.393 * originalRed + .769 * originalGreen + .189 * originalBlue > 255)
            {
                image[j][i].rgbtRed = 255;
            }
            if ((int) ((.349 * originalRed + .686 * originalGreen + .168 * originalBlue) * 10) % 10 >= 5)
            {
                image[j][i].rgbtGreen = .349 * originalRed + .686 * originalGreen + .168 * originalBlue + 1;
            }
            else
            {
                image[j][i].rgbtGreen = .349 * originalRed + .686 * originalGreen + .168 * originalBlue;
            }
            if (.349 * originalRed + .686 * originalGreen + .168 * originalBlue > 255)
            {
                image[j][i].rgbtGreen = 255;
            }
            if ((int) ((.272 * originalRed + .534 * originalGreen + .131 * originalBlue) * 10) % 10 >= 5)
            {
                image[j][i].rgbtBlue = .272 * originalRed + .534 * originalGreen + .131 * originalBlue + 1;
            }
            else
            {
                image[j][i].rgbtBlue = .272 * originalRed + .534 * originalGreen + .131 * originalBlue;
            }
            if (.272 * originalRed + .534 * originalGreen + .131 * originalBlue > 255)
            {
                image[j][i].rgbtBlue = 255;
            }
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < width / 2; i++)
    {
        for (int j = 0; j < height; j++)
        {
            image[height + 1][width + 1] = image[j][width - i - 1];
            image[j][width - i - 1] = image[j][i];
            image[j][i] = image[height + 1][width + 1];
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    float avgRed[height][width];
    float avgBlue[height][width];
    float avgGreen[height][width];
    for (int i = 0; i < width; i++)
    {
        for (int j = 0; j < height; j++)
        {
            int count = 0;
            if (i != 0 && j != 0 && i != (width - 1) && j != (height - 1))
            {
                count = 9;
                for (int k = i - 1; k < i + 2; k++)
                {
                    for (int x = j - 1; x < j + 2; x++)
                    {
                        avgRed[j][i] = avgRed[j][i] + (float) (image[x][k].rgbtRed / 9.00);
                        avgBlue[j][i] += (float) (image[x][k].rgbtBlue / 9.00);
                        avgGreen[j][i] += (float) (image[x][k].rgbtGreen / 9.00);
                    }
                }
                if ((int) (avgRed[j][i] * 10) % 10 > 4)
                {
                    avgRed[j][i] += 1;
                }
                if ((int) (avgGreen[j][i] * 10) % 10 > 4)
                {
                    avgGreen[j][i] += 1;
                }
                if ((int) (avgBlue[j][i] * 10) % 10 > 4)
                {
                    avgBlue[j][i] += 1;
                }
            }
            else
            {
                for (int k = i - 1; k < i + 2; k++)
                {
                    for (int x = j - 1; x < j + 2; x++)
                    {
                        if (x >= 0 && k >= 0 && x < height && k < width)
                        {
                            count++;
                        }
                    }
                }
                for (int k = i - 1; k < i + 2; k++)
                {
                    for (int x = j - 1; x < j + 2; x++)
                    {
                        if (x >= 0 && k >= 0 && x < height && k < width)
                        {
                            avgRed[j][i] += (float) (image[x][k].rgbtRed / (float) count);
                            avgBlue[j][i] += (float) (image[x][k].rgbtBlue / (float) count);
                            avgGreen[j][i] += (float) (image[x][k].rgbtGreen / (float) count);
                        }
                    }
                }
                if ((int) (avgRed[j][i] * 10) % 10 > 4)
                {
                    avgRed[j][i] += 1;
                }
                if ((int) (avgGreen[j][i] * 10) % 10 > 4)
                {
                    avgGreen[j][i] += 1;
                }
                if ((int) (avgBlue[j][i] * 10) % 10 > 4)
                {
                    avgBlue[j][i] += 1;
                }
            }
        }
    }
    for (int i = 0; i < width; i++)
    {
        for (int j = 0; j < height; j++)
        {
            image[j][i].rgbtRed = avgRed[j][i];
            image[j][i].rgbtBlue = avgBlue[j][i];
            image[j][i].rgbtGreen = avgGreen[j][i];
        }
    }
    return;
}
