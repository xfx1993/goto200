def minSubArrayLen(s, nums):
    """
    :type s: int
    :type nums: List[int]
    :rtype: int
    """
    tail = 0
    head = -1
    length = len(nums)
    min_length= 0
    cur_sum = 0
    for i in range(length):
        if nums[i]>=s:
            head = i
            tail = i
            cur_sum = nums[i]
            break
        cur_sum = cur_sum+nums[i]
        if cur_sum>=s:
            head = i
            break


    if head==-1:
        return 0
    if head == length-1:
        return length
    while cur_sum>=s:
        cur_sum = cur_sum-nums[tail]
        tail = tail+1
    tail = tail-1
    cur_sum = cur_sum+nums[tail]
    pre_sum = cur_sum
    min_length = head-tail+1
    while True:
        head = head+1
        if head==length:
            break
        if nums[head]>=s:
            min_length=1
            break
        cur_sum = pre_sum+nums[head]
        while cur_sum>=s:
            cur_sum = cur_sum - nums[tail]
            tail = tail + 1
        tail = tail - 1
        cur_sum = cur_sum + nums[tail]
        pre_sum = cur_sum
        min_length = min_length if head-tail+1>=min_length else head-tail+1

    return min_length

s = 7
nums = [2,3,1,2,4,3]

print(minSubArrayLen(s, nums))

