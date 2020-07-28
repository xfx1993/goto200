def wordBreak(s, wordDict):
    """
    :type s: str
    :type wordDict: List[str]
    :rtype: bool
    """
    max_wordsize=max([len(word) for word in wordDict])
    min_wordsize=min([len(word) for word in wordDict])
    max_wordsize = max_wordsize if len(s)>max_wordsize else len(s)
    dp = [False for i in range(len(s))]
    for i in range(max_wordsize):
        if s[0:i+1] in wordDict:
            dp[i]=True




    for k in range(1,len(s)):
        for j in range(k,k-max_wordsize-1,-1):
            if j<0:
                break
                if j==k and dp[j]==True:
                    break
            if dp[j]==True and k-j+1>=min_wordsize:
                if s[j+1:k+1] in wordDict:
                    dp[k]=True
                    break
    return dp[-1]


s="goalspecial"
wordDict=["go","goal","goals","special"]
print(wordBreak(s, wordDict))
