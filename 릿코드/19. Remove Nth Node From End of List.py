# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes = []
        curnode = head
        while curnode != None:
            nodes.append(curnode)
            curnode = curnode.next
        
        if n == 1:
            nextnode = None
        else:
            nextnode = nodes[len(nodes) - n +1]
        
        if len(nodes) - n  == 0:
            head = head.next
        else:
            nodes[len(nodes) - n -1].next = nextnode

        return head

        