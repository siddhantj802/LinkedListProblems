# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.reversing(None,head)
        



    def reversing(self,prev,curr):
        if curr :
            nxt = curr.next
            curr.next = prev
            
            return self.reversing(curr , nxt)
        else:
            return prev
