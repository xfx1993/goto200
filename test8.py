class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
head = ListNode(2)
node1 = ListNode(1)
# node2=ListNode(3)
# node3 = ListNode(2)
# node4 = ListNode(5)
# node5 = ListNode(2)
head.next = node1
# node1.next = node2
# node2.next = node3
# node3.next = node4
# node4.next = node5


def partition(head, x):
    """
    :type head: ListNode
    :type x: int
    :rtype: ListNode
    """
    size=1
    tail= None
    tail = head
    pre_node =None
    while tail.next:
        size +=1
        tail = tail.next


    cur_node = head
    while size!=0:
        if cur_node.val<x:
            pre_node = cur_node
            cur_node=cur_node.next
        else:
            if cur_node.next==None:
                pass
            elif pre_node==None:

                now_node = cur_node
                tail.next = now_node
                cur_node =cur_node.next
                head = cur_node
                now_node.next = None
                tail = tail.next
            else:
                now_node = cur_node
                cur_node = cur_node.next
                pre_node.next = cur_node
                tail.next = now_node
                now_node.next =None
                tail= tail.next

        size= size-1

    return head

print(partition(head,2))







