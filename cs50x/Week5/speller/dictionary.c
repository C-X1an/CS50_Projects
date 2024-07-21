// Implements a dictionary's functionality

#include <cs50.h>
#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 627;

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    int hash_key = hash(word);
    node *cursor = table[hash_key];
    while (strcasecmp(cursor->word, word) != 0)
    {
        cursor = cursor->next;
        if (cursor == NULL)
        {
            return false;
        }
    }
    if (strcasecmp(cursor->word, word) == 0)
    {
        return true;
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    int sum = 0;
    if (isalpha(word[0]) && isalpha(word[1]))
    {
        sum = (toupper(word[0]) - 'A') * (toupper(word[1]) - 'A');
        return sum;
    }
    else if ((int) word[0] == 39 || (int) word[1] == 39)
    {
        sum = 626;
    }
    return sum;
} 

// Loads dictionary into memory, returning true if successful, else false
int size_count = 0;
bool load(const char *dictionary)
{
    // TODO
    FILE *copy = fopen(dictionary, "r");
    if (copy == NULL)
    {
        return false;
    }
    char save[LENGTH + 1];
    int hash_key;
    int size = 0;
    while (fscanf(copy, "%s", save) != EOF)
    {
        size_count++;
        node *new = malloc(sizeof(node));
        new->next = NULL;
        if (new == NULL)
        {
            return false;
        }
        strcpy(new->word, save);
        hash_key = hash(save);
        if (table[hash_key] != NULL)
        {
            new->next = table[hash_key];
        }
        table[hash_key] = new;
    }
    fclose(copy);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    // done in load
    return size_count;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    for (int i = 0; i < N; i++)
    {
        node *cursor = table[i];
        node *tmp = table[i];
        while (cursor != NULL)
        {
            cursor = cursor->next;
            free(tmp);
            tmp = cursor;
        }
    }
    return true;
}
