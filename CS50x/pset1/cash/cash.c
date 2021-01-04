#include <cs50.h>
#include <stdio.h>
#include <math.h>

int main(void)
{

    // Initial variable to store change owed
    float dollars;

    // Variable to add into how many coins are owed
    int coins = 0;

    // Get input from user for amount owed
    do
    {
        dollars = get_float("Change owed: ");
    }
    while (dollars < 0);

    // Change owed made into integer to calculate number of coins;
    int cents = round(dollars * 100);


    switch (cents)
    {
        // If exact change => return immediately
        case 0:
            break;
        default:
            coins += cents / 25;
            cents %= 25;

            coins += cents / 10;
            cents %= 10;

            coins += cents / 5;
            cents %= 5;

            coins += cents;
    }

    printf("%i\n", coins);

}