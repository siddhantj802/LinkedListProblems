# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return head

        nxt = head.next


        if nxt:
            head.next = nxt.next
            nxt.next = head

            nxt.next.next = self.swapPairs(nxt.next.next)

            return nxt
        return head

        
            
