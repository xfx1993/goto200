# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

root =TreeNode(0)
node1 = TreeNode(1)
node2 = TreeNode(3)
node3=TreeNode(2)

root.left = node1
root.right = node2

node1.right =node3


def subtreeWithAllDeepest(root):
    """
    :type root: TreeNode
    :rtype: TreeNode
    """
    if not root:
        return None
    map_depth = dict()

    def dfs(now_node,map_depth):
        if not now_node:
            return 0
        depth = max([dfs(now_node.left,map_depth),dfs(now_node.right,map_depth)])+1

        map_depth[now_node]=depth

        return depth
    max_depth = dfs(root,map_depth)
    cur_node = root
    while True:
        if not cur_node.left and not cur_node.right:
            return cur_node
        elif cur_node.left and not cur_node.right:
            cur_node=cur_node.left
        elif cur_node.right and not cur_node.left:
            cur_node = cur_node.right
        elif map_depth[cur_node.left]==map_depth[cur_node.right]:
            return cur_node
        elif map_depth[cur_node.left]+1 ==map_depth[cur_node]:
            cur_node= cur_node.left
        else:
            cur_node = cur_node.right


print(subtreeWithAllDeepest(root))

