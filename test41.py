def totalHammingDistance(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    length = len(nums)

    def HammingDistace(a,b):
        c = a^b
        count = 0
        while c!=0:
            if c&1==1:
                count+=1
            c=c>>1
        return count


    res=0
    for i in range(length-1):
        for j in range(1,length):
            res+=HammingDistace(nums[i],nums[j])

    return res

nums=[4,14,2]

print(totalHammingDistance(nums))