class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def constructMaximumBinaryTree(nums):
    """
    :type nums: List[int]
    :rtype: TreeNode
    """
    def dfs(nums):
        if not nums:
            return None
        if len(nums)==1:
            return TreeNode(nums[0])

        max_num = max(nums)
        index = 0
        for i in range(len(nums)):
            if nums[i]==max_num:
                index = i
                break
        node = TreeNode(max_num)
        node.left = dfs(nums[:index])
        node.right = dfs(nums[index+1:])

    return dfs(nums)
