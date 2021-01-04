#include <stdio.h>
#include <stdlib.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>

bool isValidKey(string);
string encrypt(string, int);

int main(int argc, string argv[])
{
    // used to pass to encrypt function
    int key;

    if (argc != 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
    else
    {
        string argv1 = argv[1];

        if (!isValidKey(argv1))
        {
            printf("Usage: ./caesar key\n");
            return 1;
        }

        // cast string to int
        key = atoi(argv[1]);
    }

    string plaintext = get_string("plaintext: ");
    string ciphertext = encrypt(plaintext, key);
    printf("ciphertext: %s\n", ciphertext);
}

// check key
bool isValidKey(string key)
{
    for (int i = 0, n = strlen(key); i < n; i++)
    {
        if (!isdigit(key[i]))
        {
            return false;
        }
    }
    return true;
}

// encipher plaintext with key value
string encrypt(string plain, int key)
{
    for (int i = 0, n = strlen(plain); i < n; i++)
    {
        // letter
        if (isalpha(plain[i]))
        {
            // uppercase
            if (isupper(plain[i]))
            {
                plain[i] -= 65;
                plain[i] = (plain[i] + key) % 26;
                plain[i] += 65;
            }
            // lowercase
            else
            {
                plain[i] -= 97;
                plain[i] = (plain[i] + key) % 26;
                plain[i] += 97;
            }
        }
    }

    return plain;
}