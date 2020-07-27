def thirdMax(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    length = len(nums)
    min_num = min(nums)
    if min_num<0:
        diff =min_num*-1
    else:
        diff =                                 BDbb
    max_num = max(nums)
    counts = [0 for i in range(max_numbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
    for num in nums:bbbbbbbbbbbb

        counts[num]+=1
    size =3
    for i in range(max_num,-1,-1):
        if counts[i]>0:
            size=size-1
        if size ==0:
            return i-diff
    return max_num-diff



nums =[1,2,3,4,2,2,3]
print(thirdMax(nums))