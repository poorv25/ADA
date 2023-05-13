#include <stdio.h>
#include <stdlib.h>

#define EMPTY -1
#define DELETED -2

// Define a struct to represent the hash table
typedef struct HashTable {
    int size;
    int* keys;
    int* values;
} HashTable;

// Create a new hash table with the specified size
HashTable* createHashTable(int size) {
    HashTable* table = (HashTable*) malloc(sizeof(HashTable));
    table->size = size;
    table->keys = (int*) malloc(size * sizeof(int));
    table->values = (int*) malloc(size * sizeof(int));
    // Initialize each slot to EMPTY
    for (int i = 0; i < size; i++) {
        table->keys[i] = EMPTY;
        table->values[i] = 0;
    }
    return table;
}

// Compute the hash code for the given key
int hashCode(int key, int size) {
    return key % size;
}

// Insert a key-value pair into the hash table
void insert(HashTable* table, int key, int value) {
    // Compute the hash code for the key
    int index = hashCode(key, table->size);
    // Probe linearly until we find an empty slot or a slot with the same key
    while (table->keys[index] != EMPTY && table->keys[index] != key) {
        index = (index + 1) % table->size;
    }
    // If we found an empty slot, insert the key-value pair
    if (table->keys[index] == EMPTY) {
        table->keys[index] = key;
        table->values[index] = value;
    }
    // If we found a slot with the same key, update its value
    else {
        table->values[index] = value;
    }
}

// Lookup the value associated with the given key in the hash table
int lookup(HashTable* table, int key) {
    // Compute the hash code for the key
    int index = hashCode(key, table->size);
    // Probe linearly until we find an empty slot or a slot with the given key
    while (table->keys[index] != EMPTY) {
        if (table->keys[index] == key) {
            // If we find the key, return its value
            return table->values[index];
        }
        index = (index + 1) % table->size;
    }
    // If we reach here, the key was not found
    return -1;
}

// Delete the key-value pair with the given key from the hash table
void delete(HashTable* table, int key) {
    // Compute the hash code for the key
    int index = hashCode(key, table->size);
    // Probe linearly until we find an empty slot or a slot with the given key
    while (table->keys[index] != EMPTY) {
        if (table->keys[index] == key) {
            // If we find the key, mark the slot as DELETED
            table->keys[index] = DELETED;
            return;
        }
        index = (index + 1) % table->size;
    }
}

int main() {
    HashTable* table = createHashTable(5);

    insert(table, 1, 10);
    insert(table, 2, 20);
    insert(table, 3, 30);

    printf("Value associated with key 1: %d\n", lookup(table, 1));
    printf("Value associated with key 2: %d\n", lookup(table, 2));
}