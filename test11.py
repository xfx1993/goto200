def kSmallestPairs(nums1, nums2, k):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :type k: int
    :rtype: List[List[int]]
    """
    i = 0
    j = 0
    l_i = len(nums1)
    l_j = len(nums2)

    dp = [[] for i in range(k)]
    dp[0]=[0,0]

    for n in range(1,k):
        if j+1<=l_j-1:
            num1 = nums1[dp[n-1][0]]+nums2[dp[n-1][1]+1]
        else:
            num1 =9999999
        if i+1<=l_i-1:
            num2 = nums1[dp[n-1][0]+1]+nums2[dp[n-1][1]]
        else:
            nums2 =9999999
        if num1<num2:


