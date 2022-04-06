#Next를 처음사용해봐서 어려웟음

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        result = ListNode()
        prev = result
        carry = 0
        l1chk = True
        l2chk = True
        while l1 or l2 or carry:
            if l1 == None:
                num1 = 0
            else:
                num1 = l1.val
                l1 = l1.next
            if l2 == None:
                num2 = 0
            else:
                num2 = l2.val
                l2 = l2.next
            num3 = num1+num2+carry
            carry = num3//10
            num3 %=10
            now = ListNode()
            now.val = num3
            prev.next = now
            prev = prev.next
            
        result = result.next
        return result
            
                
        
        
        
l1 = [2,4,3]
l2 = [5,6,4]
a = Solution()
print(a.addTwoNumbers(l1,l2))