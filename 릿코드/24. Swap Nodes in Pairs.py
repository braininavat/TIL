# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        list1 = []
        list2 = []
        ans = ListNode()
        anshead = ans
        cur = head
        idx = 0
        while cur:
            if idx%2 == 0:
                list1.append(cur)
            else:
                list2.append(cur)
            idx += 1 
            cur = cur.next

        
        for i in range(len(list2)) :
            ans.next = list2[i]
            ans = ans.next
            ans.next = list1[i]
            ans = ans.next
            ans.next = None
            idx = idx+1
        
        if(len(list1) > len(list2)):
            ans.next = list1[-1]
            ans = ans.next
            ans.next = None


        return anshead.next