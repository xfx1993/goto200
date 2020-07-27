def diStringMatch(S):
    """
    :type S: str
    :rtype: List[int]
    """
    flag=[False]

    list=[]
    length = len(S)
    nums =[i for i in range(length+1)]
    all_list = []
    def dfs(nums,cen,flag):
        if flag[0] ==True:
            return
        if not nums:
            return
        if cen==length and nums:
            list.append(nums[0])
            all_list.append(list[:])
            flag[0]=True
            return


        for i in range(len(nums)):
            list.append(nums[i])
            if S[cen]=='I':
                dfs(nums[i+1:],cen+1,flag)
            else:
                dfs(nums[:i],cen+1,flag)
            list.pop()


    dfs(nums,0,flag)
    return all_list[0]

S="DDIDDIIDIIIIDDIIDIDIDIIIIDIIIDDDDIIDIIIIDIDDIIDIDI"
print(diStringMatch(S))