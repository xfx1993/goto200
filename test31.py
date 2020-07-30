def maximumProduct(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums_sort = sorted(nums)
    return max([nums_sort[-1]*nums_sort[-2]*nums_sort[-3],nums_sort[-1]*nums_sort[0]*nums_sort[1]])

nums = [1,2,3,4,-1,-8]
print(maximumProduct(nums))