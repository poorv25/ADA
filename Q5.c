#include <stdio.h>

void merge(int arr[], int left[], int left_size, int right[], int right_size)
{
    int i = 0, j = 0, k = 0;
    // Merge left and right subarrays into arr
    while (i < left_size && j < right_size)
    {
        if (left[i] <= right[j])
        {
            arr[k++] = left[i++];
        }
        else
        {
            arr[k++] = right[j++];
        }
    }
    // Copy any remaining elements from left subarray to arr
    while (i < left_size)
    {
        arr[k++] = left[i++];
    }
    // Copy any remaining elements from right subarray to arr
    while (j < right_size)
    {
        arr[k++] = right[j++];
    }
}

void mergeSort(int arr[], int n)
{
    if (n > 1)
    {
        int mid = n / 2;
        int left[mid], right[n - mid];
        // Split arr into left and right subarrays
        for (int i = 0; i < mid; i++)
        {
            left[i] = arr[i];
        }
        for (int i = mid; i < n; i++)
        {
            right[i - mid] = arr[i];
        }
        // Recursively sort left and right subarrays
        mergeSort(left, mid);
        mergeSort(right, n - mid);
        // Merge sorted left and right subarrays into arr
        merge(arr, left, mid, right, n - mid);
    }
}

int main()
{
    int arr[] = {64, 34, 25, 12, 22, 11, 90};
    int n = sizeof(arr) / sizeof(arr[0]);

    mergeSort(arr, n);

    printf("Sorted array: ");
    for (int i = 0; i < n; i++)
    {
        printf("%d ", arr[i]);
    }

    return 0;
}
