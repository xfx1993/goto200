def divisorGame( N):
    """
    :type N: int
    :rtype: bool
    """
    dp = [False for i in range(N+1)]
    dp[0]=False
    dp[1]=False
    dp[2]=True

    for i in range(1,N+1):
        flag = False
        for j in range(1,i):
            if i%j==0:
                if dp[i-j]==True:
                    flag =True
                    break
            dp[i]=not flag


    return dp[-1]

print(divisorGame(6))