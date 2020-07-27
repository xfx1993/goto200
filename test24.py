def reorganizeString(S):
    """
    :type S: str
    :rtype: str
    """
    map_count = dict()
    size = len(S)
    for ch in S:
        if ch not in map_count:
            map_count[ch]=1
        else:
            map_count[ch]+=1
    max_count =0
    list_char = []
    stack = []
    for item in map_count.items():
        list_char.append(item[0])
        stack.append(item[1])
        if item[1]>max_count:
            max_count = item[1]



    if max_count==1:
        return S
    if max_count-1>len(S)-max_count:
        return ""
    result = ''
    while size!=0:
        flag =False
        for i in range(len(stack)):
            if flag  and stack[i]==1:
                continue
            else:
                flag = False

            if stack[i]!=0:
                result+=list_char[i]
                stack[i]-=1
                size-=1
                if stack[i]==0:
                    flag=True
                    continue
    return result

S = "baaba"
print(reorganizeString(S))