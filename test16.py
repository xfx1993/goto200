class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

head1 = ListNode(1)
head2 = ListNode(0)
# head3 = ListNode(2)
# node1 =ListNode(4)
# node2 =ListNode(5)
# node3 =ListNode(3)
# node4 =ListNode(4)
# node5 =ListNode(6)
# head1.next = node1
# node1.next = node2
#
# head2.next = node3
# node3.next = node4
#
# head3.next = node5



def mergeKLists(lists):
    """
    :type lists: List[ListNode]
    :rtype: ListNode
    """


    def merge(lists):
        length = len(lists)
        if length==1:
            return lists[0]
        if length==2:
            head1 = lists[0]
            head2 = lists[1]
            head = ListNode(-9999999)
            curnode = head
            curnode1= head1
            curnode2 = head2
            while True:
                if curnode1==None and curnode2 ==None:
                    break
                elif curnode1==None and curnode2!=None:
                    node = ListNode(curnode2.val)
                    curnode.next = node
                    curnode = curnode.next
                    curnode2 = curnode2.next
                elif curnode2==None and curnode1!=None:
                    node = ListNode(curnode1.val)
                    curnode.next = node
                    curnode = curnode.next
                    curnode1 = curnode1.next
                elif curnode1.val<curnode2.val:
                    node =ListNode(curnode1.val)
                    curnode.next = node
                    curnode = curnode.next
                    curnode1 = curnode1.next
                else:
                    node = ListNode(curnode2.val)
                    curnode.next = node
                    curnode = curnode.next
                    curnode2 = curnode2.next
            head = head.next
            return head
        s_e = length//2
        head_1 = merge(lists[0:s_e])
        head_2 = merge(lists[s_e:])

        return merge([head_1,head_2])


    return merge(lists)

print(mergeKLists([head1,head2]))

