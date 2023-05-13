#include <stdio.h>

int binarySearch(int arr[], int left, int right, int target) {
    while (left <= right) {
        int mid = left + (right - left) / 2;

        if (arr[mid] == target) {
            return mid;
        }
        else if (arr[mid] < target) {
            left = mid + 1;
        }
        else {
            right = mid - 1;
        }
    }

    return -1; // target not found
}

int main() {
    int arr[] = { 2, 5, 8, 12, 16, 23, 38, 56, 72, 91 };
    int n = sizeof(arr) / sizeof(arr[0]);

    int target = 16;
    int result = binarySearch(arr, 0, n - 1, target);

    if (result == -1) {
        printf("Element not present in array\n");
    }
    else {
        printf("Element found at index %d\n", result);
    }

    return 0;
}
