class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def maxDepth(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    cur_node = root
    def dfs(cur_node,level):
        if not cur_node.left and not cur_node.right:
            return level

        if cur_node.left:
            left_level = dfs(cur_node.left,level+1)
        if cur_node.right:
            right_level = dfs(cur_node.right,level+1)

        return max([left_level,right_level])
    return dfs(cur_node,0)