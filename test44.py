def findLeastNumOfUniqueInts( arr, k):
    """
    :type arr: List[int]
    :type k: int
    :rtype: int
    """
    dic = dict()

    length = len(arr)

    for i in range(length):
        if arr[i] not in dic:
            dic[arr[i]]=1
        else:
            dic[arr[i]]+=1

    dic_list = [item for item in dic.items()]

    dic_list.sort(key=lambda x :x[1],reverse=True)
    result = len(dic_list)
    while k>0:
        k = k-dic_list[-1][1]
        result=result-1
        dic_list.pop()

    if k==0:
        return result
    else:
        return result+1

arr = [4,3,1,1,3,3,2]
k = 3

print(findLeastNumOfUniqueInts(arr,k))