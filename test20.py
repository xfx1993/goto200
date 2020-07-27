def intersect( nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    max1 = max(nums1)
    max2 = max(nums2)
    max  = max([max1,max2])
    

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]

print(intersect(nums1,nums2))
