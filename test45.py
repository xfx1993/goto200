def findLength(A, B):
    """
    :type A: List[int]
    :type B: List[int]
    :rtype: int
    """
    length_A = len(A)
    length_B =len(B)

    dp = [[0 for i in range(length_B)] for j in range(length_A)]

    for i in range(length_A):
        for  j in range(length_B):
            if A[i]!=B[j]:
                dp[i][j]=0
            else:
                if i==0 or j==0:
                    dp[i][j]=1
                else:
                    dp[i][j]=dp[i-1][j-1]+1

    return max([max(i) for i in dp])

A=[1,2,3,2,1,4]
B=[3,2,1,4,7,1,2,3,2,1]

print(findLength(A,B))