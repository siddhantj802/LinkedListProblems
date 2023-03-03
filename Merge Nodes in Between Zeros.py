# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode()
        dummy = ans
        curr = head

        while curr and curr.next:
            count = 0
            if curr.val == 0:
                count = 0
                curr = curr.next
            while curr and curr.val != 0 :
                count += curr.val
                curr = curr.next

            dummy.next = ListNode(count)
            dummy = dummy.next


        return ans.next
        

      
        
        
        
            
        


