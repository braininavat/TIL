# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#1년만에 알고리즘 다시 풀었는데 이전에 푼문제였음...
#얕은복사 과정이 헷갈림. 첫 시도에서 return이 끝 노드만 반환.
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        carry = 0
        resnode = None
        curnode = None

        while(True):

            if(l1 == None and l2 == None) : break;
                       
            if(l1 == None): l1val = 0
            else: l1val = l1.val
            if(l2 == None): l2val = 0
            else: l2val = l2.val
    
            res = l1val + l2val + carry

            if(res > 9) : 
                res -= 10
                carry = 1
            else : 
                carry = 0
            
            if(resnode == None):
                resnode = ListNode()
                curnode = resnode
            else: 
                curnode.next = ListNode()
                curnode = curnode.next
            
            curnode.val = res
                
            if(l1 != None): l1 = l1.next 
            if(l2 != None): l2 = l2.next
            
        if(carry == 1):
            curnode.next = ListNode(carry)

        return resnode