#include <stdio.h>

int linearSearch(int arr[], int n, int x) {
    // Loop through the array and check each element
    for (int i = 0; i < n; i++) {
        if (arr[i] == x) {
            // If we find the element, return its index
            return i;
        }
    }
    // If we reach here, the element was not found
    return -1;
}

int main() {
    int arr[] = { 5, 10, 15, 20, 25 };
    int n = sizeof(arr) / sizeof(arr[0]);
    int x = 15;

    int result = linearSearch(arr, n, x);

    if (result == -1) {
        printf("Element not found\n");
    } else {
        printf("Element found at index %d\n", result);
    }

    return 0;
}
