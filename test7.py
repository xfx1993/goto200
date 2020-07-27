class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


left2 = TreeNode(2)
right2 =TreeNode(4)
left3 = TreeNode(1)
left1 = TreeNode(3)
right1 = TreeNode(6)
root = TreeNode(5)
root.left = left1
root.right = right1

left1.left = left2
left1.right = right2
left2.left = left3

root2 = TreeNode(2)
root2.left = TreeNode(1)

def isSubtree(s,t):
    """
    :type s: TreeNode
    :type t: TreeNode
    :rtype: bool
    """

    flag = [False]
    def dfs(cur_root,flag,t_list):
        if flag[0]==True:
            return ''
        list =''
        if not cur_root:
            return ''
        if cur_root:
           list = dfs(cur_root.left,flag,t_list)+str(cur_root.val)+dfs(cur_root.right,flag,t_list)
           if t_list==list:
                flag[0]=True
           return list

    def dfs2(cur_root):
        list =''
        if not cur_root:
            return ''
        if cur_root:
           list = dfs2(cur_root.left)+str(cur_root.val)+dfs2(cur_root.right)
           return list

    t_2 = dfs2(t)
    dfs(s, flag, t_2)

    return flag[0]




print(isSubtree(root,root2))
