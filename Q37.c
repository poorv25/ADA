#include <stdio.h>
#include <stdlib.h>

/* Function to swap two integers */
void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

/* Function to partition the array around a pivot element */
int partition(int arr[], int left, int right) {
    int pivot = arr[right]; // choose last element as pivot
    int i = left - 1; // index of smaller element
    for (int j = left; j <= right - 1; j++) {
        if (arr[j] >= pivot) { // if current element is greater than or equal to pivot
            i++; // increment index of smaller element
            swap(&arr[i], &arr[j]);
        }
    }
    swap(&arr[i+1], &arr[right]);
    return i+1; // return index of pivot element
}

/* Function to find the kth largest element in an array using divide-and-conquer */
int find_kth_largest(int arr[], int left, int right, int k) {
    if (k > 0 && k <= right - left + 1) { // check if k is within range
        int pivot_idx = partition(arr, left, right); // partition the array around a pivot element
        int size = pivot_idx - left + 1; // size of the left subarray
        if (size == k) { // if the size of the left subarray is equal to k
            return arr[pivot_idx]; // the pivot element is the kth largest element
        } else if (size > k) { // if the size of the left subarray is greater than k
            return find_kth_largest(arr, left, pivot_idx - 1, k); // search in the left subarray
        } else { // if the size of the left subarray is less than k
            return find_kth_largest(arr, pivot_idx + 1, right, k - size); // search in the right subarray for (k - size)th largest element
        }
    }
    return -1; // return -1 if k is out of range
}

/* Example usage */
int main() {
    int arr[] = {3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5}; // example array
    int n = sizeof(arr) / sizeof(arr[0]); // size of the array
    int k = 4; // find the 4th largest element
    int kth_largest = find_kth_largest(arr, 0, n - 1, k);
    printf("%dth largest element: %d\n", k, kth_largest);
    return 0;
}
