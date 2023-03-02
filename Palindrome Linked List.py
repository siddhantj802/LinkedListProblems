# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        s = ""
        revS = ""
        
        while head:
            s = s + str(head.val)
            head = head.next

        revS = s[::-1]

        if s == revS:
            return True
        else:
            return False

        
