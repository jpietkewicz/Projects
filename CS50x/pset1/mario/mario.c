#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int height = 0;
    do
    {
        height = get_int("Height: ");
    }
    while (height < 1 || height > 8);

    for (int i = 1; i <= height; i++)
    {
        // print spaces descending from height - 1 to 0
        for (int j = height - i; j > 0; j--)
        {
            printf(" ");
        }

        // print # for left pyramid
        for (int k = 0; k < i; k++)
        {
            printf("#");
        }

        // print spaces in between
        printf("  ");

        // print right pyramid
        for (int m = 0; m < i; m++)
        {
            printf("#");
        }

        printf("\n");
    }

}