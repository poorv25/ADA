#include <stdio.h>
#include <stdlib.h>

// Define a struct to represent each node in the linked list
typedef struct Node {
    int key;
    int value;
    struct Node* next;
} Node;

// Define a struct to represent the hash table
typedef struct HashTable {
    int size;
    Node** buckets;
} HashTable;

// Create a new node with the specified key and value
Node* createNode(int key, int value) {
    Node* newNode = (Node*) malloc(sizeof(Node));
    newNode->key = key;
    newNode->value = value;
    newNode->next = NULL;
    return newNode;
}

// Create a new hash table with the specified size
HashTable* createHashTable(int size) {
    HashTable* table = (HashTable*) malloc(sizeof(HashTable));
    table->size = size;
    table->buckets = (Node**) malloc(size * sizeof(Node*));
    // Initialize each bucket to NULL
    for (int i = 0; i < size; i++) {
        table->buckets[i] = NULL;
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
    // Create a new node with the key-value pair
    Node* newNode = createNode(key, value);
    // Insert the new node into the linked list at the appropriate bucket
    newNode->next = table->buckets[index];
    table->buckets[index] = newNode;
}

// Lookup the value associated with the given key in the hash table
int lookup(HashTable* table, int key) {
    // Compute the hash code for the key
    int index = hashCode(key, table->size);
    // Traverse the linked list at the appropriate bucket to find the key-value pair
    Node* current = table->buckets[index];
    while (current != NULL) {
        if (current->key == key) {
            // If we find the key, return its value
            return current->value;
        }
        current = current->next;
    }
    // If we reach here, the key was not found
    return -1;
}

int main() {
    HashTable* table = createHashTable(5);

    insert(table, 1, 10);
    insert(table, 2, 20);
    insert(table, 3, 30);

    printf("Value associated with key 1: %d\n", lookup(table, 1));
    printf("Value associated with key 2: %d\n", lookup(table, 2));
    printf("Value associated with key 3: %d\n", lookup(table, 3));
    printf("Value associated with key 4: %d\n", lookup(table, 4));

    return 0;
}
