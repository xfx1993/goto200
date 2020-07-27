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


def binaryTreePaths(root):
    """
    :type root: TreeNode
    :rtype: List[str]
    """
    all_list =[]
    list1=[]


    def dfs(list1,node_list):
        if node_list[0]==None and node_list[1]==None:
            all_list.append(list1[:])
            return
        for node in node_list:
            if node==None:
                continue
            else:
                list1.append(str(node.val))
                dfs(list1,[node.left,node.right])
                list1.pop()


    dfs(list1,[root])
    result =[]
    for l in all_list:
        str1=''
        size = len(l)
        for i in range(size):
            if i!=size-1:
                str1=str1+l[i]+'->'
            else:
                str1 +=l[i]

        result.append(str1)

    return result

print(binaryTreePaths(root))







