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
    flag= True
    flag1 = True
    if not root:
        return True
    if root.left:
        if root.val>root.left.val:
            flag = True
        else:
            flag = False
    if root.right:
        if root.val<root.right.val:
            flag1 = True
        else:
            flag1 =False
    return flag and flag1 and isValidBST(root.left) and isValidBST(root.right)