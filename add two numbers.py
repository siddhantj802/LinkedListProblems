# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ans = ListNode(0)
        curr1 = l1
        curr2 = l2
        carry = 0
        
        while curr1 or curr2 or carry:
            sum = 0
            if curr1:
                sum += curr1.val
                curr1 = curr1.next
            if curr2:
                sum += curr2.val
                curr2 = curr2.next

            sum += carry
            carry = sum//10

            dummy.next = ListNode(sum%10)
            dummy = dummy.next

        return ans.next
        


        
        
