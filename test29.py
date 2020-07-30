def findSpecialInteger(arr):
    """
    :type arr: List[int]
    :rtype: int
    """
    length = len(arr)
    min_count = (length//4)+1

    count =1

    for i in range(length):
        if i==0:
            continue
        if arr[i]==arr[i-1]:
            count=count+1

        if arr[i]!=arr[i-1]:
            count=1
        if count>=min_count:
            return arr[i]


