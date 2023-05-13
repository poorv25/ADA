def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def kth_largest_element(arr, low, high, k):
    if k > 0 and k <= high - low + 1:
        pivot_index = partition(arr, low, high)
        if pivot_index - low == k - 1:
            return arr[pivot_index]
        elif pivot_index - low > k - 1:
            return kth_largest_element(arr, low, pivot_index - 1, k)
        else:
            return kth_largest_element(arr, pivot_index + 1, high, k - pivot_index + low - 1)