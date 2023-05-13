def merge(arr1, arr2):
    n1, n2 = len(arr1), len(arr2)
    i, j, k = 0, 0, 0
    merged = [0] * (n1 + n2)
    
    while i < n1 and j < n2:
        if arr1[i] <= arr2[j]:
            merged[k] = arr1[i]
            i += 1
        else:
            merged[k] = arr2[j]
            j += 1
        k += 1
    
    while i < n1:
        merged[k] = arr1[i]
        i += 1
        k += 1
    
    while j < n2:
        merged[k] = arr2[j]
        j += 1
        k += 1
    
    return merged

def merge_sort(arr):
    n = len(arr)
    if n > 1:
        mid = n // 2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])
        arr = merge(left, right)
    return arr
