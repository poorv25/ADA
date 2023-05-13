#include <stdio.h>
#include <stdlib.h>

typedef struct Heap {
    int* array;
    int size;
    int capacity;
} Heap;

Heap* createHeap(int capacity) {
    Heap* heap = (Heap*) malloc(sizeof(Heap));
    heap->array = (int*) malloc(capacity * sizeof(int));
    heap->size = 0;
    heap->capacity = capacity;
    return heap;
}

void swap(int* x, int* y) {
    int temp = *x;
    *x = *y;
    *y = temp;
}

void insert(Heap* heap, int value) {
    if (heap->size == heap->capacity) {
        printf("Error: Heap is full.\n");
        return;
    }
    heap->array[heap->size] = value;
    int index = heap->size;
    while (index > 0 && heap->array[index] > heap->array[(index - 1) / 2]) {
        swap(&heap->array[index], &heap->array[(index - 1) / 2]);
        index = (index - 1) / 2;
    }
    heap->size++;
}

void heapify(Heap* heap, int index) {
    int left = 2 * index + 1;
    int right = 2 * index + 2;
    int largest = index;
    if (left < heap->size && heap->array[left] > heap->array[largest]) {
        largest = left;
    }
    if (right < heap->size && heap->array[right] > heap->array[largest]) {
        largest = right;
    }
    if (largest != index) {
        swap(&heap->array[index], &heap->array[largest]);
        heapify(heap, largest);
    }
}

int extractMax(Heap* heap) {
    if (heap->size == 0) {
        printf("Error: Heap is empty.\n");
        return -1;
    }
    int max = heap->array[0];
    heap->size--;
    heap->array[0] = heap->array[heap->size];
    heapify(heap, 0);
    return max;
}

void heapSort(int* array, int size) {
    Heap* heap = createHeap(size);
    for (int i = 0; i < size; i++) {
        insert(heap, array[i]);
    }
    for (int i = 0; i < size; i++) {
        array[i] = extractMax(heap);
    }
}

int main() {
    int array[] = {5, 3, 8, 4, 2, 7, 1, 6};
    int size = sizeof(array) / sizeof(int);

    printf("Original array:\n");
    for (int i = 0; i < size; i++) {
        printf("%d ", array[i]);
    }
    printf("\n");

    heapSort(array, size);

    printf("Sorted array:\n");
    for (int i = 0; i < size; i++) {
        printf("%d ", array[i]);
    }
    printf("\n");

    return 0;
}
