#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

bool isValidKey(string);
string substitute(string);

int main(int argc, string argv[])
{
    // Check if key is supplied and nothing else
    if (argc != 2)
    {
        printf("Usage: ./substitution key\n");
        return 1;
    }
    // Check if key is valid string
    if (isValidKey(argv[1]))
    {
        string plaintext = get_string("plaintext: ");

        string ciphertext = substitute(plaintext);

        printf("ciphertext: %s\n", ciphertext);
        return 0;
    }
    else
    {
        return 1;
    }

}

bool isValidKey(string key)
{
    bool result = true;

    if (strlen(key) != 26)
    {
        result = false;
    }

    return result;
}

string substitute(string plain)
{
    string result = NULL;



    return result;
}