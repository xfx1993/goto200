def minimalSteps(self, maze):
    """
    :type maze: List[str]
    :rtype: int
    """
    start_list = []
    end_list =[]


    start_end_cost=dict()

    end_cost = dict()

    row = len(maze)
    col = len(maze(0))
    flag = [[0 for i in range(col)] for i in range(row)]
    start=[]
    for i in range(row):
        for j in range(col)
            if maze[i][j]=='S':
                start =[i,j]
                start_list.append([i,j])
                start_end_cost[[i,j]]=dict()
            if maze[i][j]=='M':
                start_list.append([i, j])
                start_end_cost[[i, j]] = dict()
            if maze[i][j]=="O":
                end_list.append([i,j])
                start_end_cost[[i, j]] = dict()

    for s in start_list:
        stack = s[:]
        cen = 0
        cur_flag =flag[:]
        cur_flag[s[0][0]][s[0][1]]=1
        while stack:
            cur_stack =[]
            cen = cen +1
            for pos in stack:
                x= pos[0]
                y = pos[1]
                if x-1>=0 and maze[x-1][y]!='#' and cur_flag[x-1][y]==0:
                    cur_stack.append([x-1,y])
                    cur_flag[x-1][y]=1
                    if maze[x-1][y]=='O':
                        start_end_cost[[s[0][0],s[0][1]]][[x-1,y]]=cen
                        start_end_cost[[x-1,y]][[s[0][0],s[0][1]]]=cen
                if y-1>=0 and maze[x][y-1]!="#" and cur_flag[x][y-1]==0:
                    cur_stack.append([x,y-1])
                    cur_flag[x][y-1]=1
                    if maze[x][y-1]=='O':
                        start_end_cost[[s[0][0],s[0][1]]][[x,y-1]]=cen
                        start_end_cost[[x,y-1]][[s[0][0],s[0][1]]]=cen
                if x+1<=row-1 and maze[x+1][y]!='#' and cur_flag[x+1][y]==0:
                    cur_stack.append([x+1,y])
                    cur_flag[x+1][y]=1
                    if maze[x+1][y]=='O':
                        start_end_cost[[s[0][0],s[0][1]]][[x+1,y]]=cen
                        start_end_cost[[x+1,y]][[s[0][0],s[0][1]]]=cen
                if y+1<=col-1 and maze[x][y+1]!='#' and cur_flag[x][y+1]==0:
                    cur_stack.append([x,y+1])
                    cur_flag[x][y+1]=1
                    if maze[x][y+1]=='O':
                        start_end_cost[[s[0][0],s[0][1]]][[x,y+1]]=cen
                        start_end_cost[[x,y+1]][[s[0][0],s[0][1]]]=cen


