def uniqueLetterString( s):
    """
    :type s: str
    :rtype: int
    """
    all_count = [0]

    def uniqueWordCount(words):
        count_map = dict()
        for word in words:
            if word not in count_map:
                count_map[word]=1
            else:
                count_map[word]+=1
        result =0
        for key,vlaue in count_map.items():
            if vlaue==1:
                result+=1
        return result
    def dfs(s,index,str_sub,all_count):

        str_sub.append(s[index])
        all_count[0]+=uniqueWordCount(str_sub)
        if index==len(s)-1:
            return
        dfs(s,index+1,str_sub,all_count)

    for k in range(len(s)):
        str_sub = []

        dfs(s,k,str_sub,all_count)

    return all_count[0]%(10**9+7)



s = "LEETCODE"
print(uniqueLetterString( s))