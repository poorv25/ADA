def max_subarray(nums):
    if not nums:
        return 0
    
    max_sum = nums[0]
    cur_sum = nums[0]
    
    for num in nums[1:]:
        cur_sum = max(num, cur_sum + num)
        max_sum = max(max_sum, cur_sum)
    
    return max_sum
