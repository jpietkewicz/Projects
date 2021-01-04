// Implements a dictionary's functionality

#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>
#include <ctype.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// Number of words added to hash table
int numWords = 0;
unsigned int hashValue;

// Number of buckets in hash table
const unsigned int N = 26;

// Hash table
node *table[N];

// Returns true if word is in dictionary else false
bool check(const char *word)
{
    hashValue = hash(word);
    node *cursor = table[hashValue];

    while (cursor != NULL)
    {
        if (strcasecmp(cursor->word, word) == 0)
        {
            return true;
        }
        cursor = cursor->next;
    }

    return false;
}

// Hashes word to a number
// https://stackoverflow.com/questions/20462826/hash-function-for-strings-in-c
unsigned int hash(const char *word)
{
    unsigned long hash = 5381;
    int n;
    while ((n = toupper(*word++)))
    {
        hash = ((hash << 5) + hash) + n;
    }
    return hash % N;
}

// Loads dictionary into memory, returning true if successful else false
bool load(const char *dictionary)
{
    // open up file
    FILE *dic = fopen(dictionary, "r");
    if (dic == NULL)
    {
        printf("Failed to open file.");
        return false;
    }
    // read from file
    char dicWord[LENGTH + 1];

    while (fscanf(dic, "%s", dicWord) != EOF)
    {
        node *n = malloc(sizeof(node));
        if (n == NULL)
        {
            fclose(dic);
            return false;
        }

        // store dicWord into node
        strcpy(n->word, dicWord);

        //hash value
        hashValue = hash(dicWord);
        // point new node to next index
        n->next = table[hashValue];
        // place node at beginning of list
        table[hashValue] = n;

        // add 1 to numWords every iteration through hashing
        numWords++;
    }

    fclose(dic);
    return true;
}

// Returns number of words in dictionary if loaded else 0 if not yet loaded
unsigned int size(void)
{
    return numWords;
}

// Unloads dictionary from memory, returning true if successful else false
bool unload(void)
{
    for (int i = 0; i < N; i++)
    {
        node *tmp = table[i];
        while (tmp != NULL)
        {
            node *cursor = tmp;
            tmp = tmp->next;
            free(cursor);
        }
    }
    return true;
}
