def bubble_sort(arr):
  
    n = len(arr)

    for i in range(n):
        # Last i elements are already in place
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                # Swap adjacent elements if they are in the wrong order
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr
