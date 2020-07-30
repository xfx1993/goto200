def decompressRLElist( nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    length = len(nums)
    index_num=1
    index_count = 0
    result=[]
    while index_num<=length-1:
        result.extend([nums[index_num]]*nums[index_count])
        index_num +=2
        index_count+=2
    return result

nums = [1,1,3,4]
print(decompressRLElist( nums))