def maxSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if max(nums)<0:
        return max(nums)
    slow =0
    fast =0
    max_sum =-101
    pre_sum =0
    while fast<len(nums):
        if slow== fast and nums[slow]<0:
            slow+=1
            fast+=1
        elif slow==fast and nums[slow]>=0:
            if nums[slow]>max_sum:
                max_sum = nums[slow]
            pre_sum = nums[slow]
            fast +=1
        elif pre_sum+nums[fast]<0:
            fast =fast+1
            slow = fast
        elif pre_sum+nums[fast]>=0:
            if pre_sum+nums[fast]>max_sum:
                max_sum = pre_sum+nums[fast]
            pre_sum = pre_sum+nums[fast]
            fast = fast + 1
    return max_sum


nums = [-2,1,-3,4,-1,2,1,-5,4]

print(maxSubArray(nums))
