class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def isValidBST(root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    stack = []
    cur_node = root
    result = []

    while stack or cur_node:
        while cur_node:
            stack.append(cur_node)
            cur_node = cur_node.left
        now_node = stack.pop()
        if result and now_node.val<=result[-1]:
            return False
        result.append(now_node.val)
        cur_node = now_node.right

    return True

