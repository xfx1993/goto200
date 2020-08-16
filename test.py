1，twosum


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def mergeTrees( t1, t2):
    """
    :type t1: TreeNode
    :type t2: TreeNode
    :rtype: TreeNode
    """
    if t1 and t2:
        t1.val = t1.val+t2.val
    def dfs(t1,t2):
        if not t1.left and not not t2.left and not t1.right and not t2.right:
            return
        if t1.left and t2.left:
            t1.left.val = t2.left.val+t1.left.val
            dfs(t1.left,t2.left)
        if t1.right and t2.right:
            t1.right.val = t2.right.val + t1.right.val
            dfs(t1.right,t2.right)
        if not t1.left and t2.left:
            t1.left = TreeNode(t2.left.val)
            dfs(t1.left, t2.left)
        if not t2.right and t2.right:
            t2.right = TreeNode(t2.right.val)
            dfs(t1.left, t2.left)

    dfs(t1,t2)
    return t1
