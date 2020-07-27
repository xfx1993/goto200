def change(amount, coins):
    """
    :type amount: int
    :type coins: List[int]
    :rtype: int
    """
    dp = [0 for i in range(amount+1)]
    dp[0]=1
    for coin in coins:
        for i in range(1,amount+1):
            if i-coin>=0:
                dp[i] =dp[i]+dp[i-coin]

    return dp[-1]

amount = 5
coins = [1, 2, 5]
print(change(amount, coins))