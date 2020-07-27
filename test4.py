class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


left2 = TreeNode(2)
right2 =TreeNode(4)
left3 = TreeNode(1)
left1 = TreeNode(-100)
right1 = TreeNode(6)
root = TreeNode(5)
root.left = left1
root.right = right1

left1.left = left2
left1.right = right2
left2.left = left3



def levelOrder(root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    stack=[]
    stack.append(root)
    cen =[[root.val]]
    while stack:
        cur_stack=[]
        cur_cen = []
        for node in stack:
            if node.left:
                cur_stack.append(node.left)
                cur_cen.append(node.left.val)
            if node.right:
                cur_stack.append(node.right)
                cur_cen.append(node.right.val)
        if cur_cen:
            cen.append(cur_cen)
        stack=cur_stack[:]

    return cen

print(levelOrder(root))
