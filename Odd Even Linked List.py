# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        even = head.next
        odd = head
        evenhead = head.next

        while odd and even and odd.next and even.next:
            odd.next = even.next
            odd = self.oddEvenList(odd.next)
            even.next = odd.next
            even = self.oddEvenList(evem.next)

            return odd

        odd.next = evenhead

        return head
        

    
