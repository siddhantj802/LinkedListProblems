# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        temp = head
        length = 0
        result = 0

        while(temp.next):
            length += 1
            temp = temp.next
        
        while(length>=0):
            result = result + head.val * (2 ** length)
            length = length - 1
            head = head.next
        return result
            

        
