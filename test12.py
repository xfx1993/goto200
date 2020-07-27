def maximalSquare(matrix):
    """
    :type matrix: List[List[str]]
    :rtype: int
    """
    row =len(matrix)
    col = len(matrix[0])

    for i in range(row):
        if matrix[i][0]==1:
            if matrix[i][1]==0:
                matrix[i][0]=0
        if matrix[i][col-1]==1:
            if matrix[i][col-2]==0:
                matrix[i][col-1]=0
    for i in range(col):
        if matrix[0][i]==1

