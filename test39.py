def countArrangement(N):
    """
    :type N: int
    :rtype: int
    """
    if N==1:
        return 1
    init_list = [i for i in range(1,N+1)]

    cen =1
    stack = []
    count =[0]
    def dfs(cur_list,cen,stack,count):
        if cen==N+1:
            count[0]+=1
            return
        for i in range(len(cur_list)):
            if cen%cur_list[i]==0 or cur_list[i]%cen==0:
                stack.append(cur_list[i])
                dfs(cur_list[0:i]+cur_list[i+1:],cen+1,stack,count)
                stack.pop()
            else:
                continue

    dfs(init_list, 1, stack, count)
    return count[0]

print(countArrangement(3))
