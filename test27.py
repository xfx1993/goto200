def wordBreak(s, wordDict):
    """
    :type s: str
    :type wordDict: List[str]
    :rtype: bool
    """
    def createListStart(s,wordDict):
        list_s = []
        for word in wordDict:
            if s.startswith(word):
                list_s.append(word)
        return list_s
    list_start = createListStart(s,wordDict)
    flag =[False]
    def dfs(s,list_start,wordDict):
        if flag[0]==True:
            return
        if not s:
            flag[0]=True

        if s and not list_start:
            return

        for w in list_start:
            length = len(w)
            s= s[length:]
            cur_list_start = createListStart(s,wordDict)
            dfs(s, cur_list_start, wordDict)
            s =w+s

    dfs(s,list_start,wordDict)
    return flag[0]


s = "applepenapplele"
wordDict = ["apple", "pen"]
print(wordBreak(s, wordDict))


