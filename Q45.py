def max_subarray_sum(arr, low, high):
    # Base case: only one element in the array
    if low == high:
        return arr[low]

    mid = (low + high) // 2

    # Recursively find the maximum subarray sum in the left and right subarrays
    left_sum = max_subarray_sum(arr, low, mid)
    right_sum = max_subarray_sum(arr, mid + 1, high)

    # Find the maximum subarray sum that includes the middle element
    max_left_sum = float('-inf')
    left_temp_sum = 0
    for i in range(mid, low - 1, -1):
        left_temp_sum += arr[i]
        if left_temp_sum > max_left_sum:
            max_left_sum = left_temp_sum

    max_right_sum = float('-inf')
    right_temp_sum = 0
    for i in range(mid + 1, high + 1):
        right_temp_sum += arr[i]
        if right_temp_sum > max_right_sum:
            max_right_sum = right_temp_sum

    # Return the maximum subarray sum among the left subarray, right subarray, and the subarray that crosses the midpoint
    return max(left_sum, right_sum, max_left_sum + max_right_sum)
