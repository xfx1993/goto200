def longestIncreasingPath(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: int
    """


    row = len(matrix)
    col = len(matrix[0])
    visit = [[0 for i in range(col)] for j in range(row)]
    count_list = [0]

    def dfs(pos,visit,matrix,stack_length):
        if not pos:
            count_list[0] =count_list[0] if count_list[0]>stack_length[0] else stack_length[0]
            return


        for p in pos:
            x = p[0]
            y = p[1]
            visit[x][y]=1
            stack_length[0]+=1
            next_pos = []
            if x-1>=0 and matrix[x-1][y]>matrix[x][y]:
                next_pos.append([x-1,y])
            if x+1<=row-1 and matrix[x+1][y]>matrix[x][y]:
                next_pos.append([x+1,y])
            if y-1>=0 and matrix[x][y-1]>matrix[x][y]:
                next_pos.append([x,y-1])
            if y+1<=col-1 and matrix[x][y+1]>matrix[x][y]:
                next_pos.append([x,y+1])
            dfs(next_pos,visit,matrix,stack_length)
            stack_length[0]-=1




    for i in range(row):
        for j in range(col):
            stack_length = [0]
            if visit[i][j]==0:
                dfs([[i,j]],visit,matrix,stack_length)
    return count_list[0]

matrix =[
  [9,10,4],
  [6,6,8],
  [2,1,1]
]
print(longestIncreasingPath(matrix))
