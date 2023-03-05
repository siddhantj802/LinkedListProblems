# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swap(self,arr,k):
        n = len(arr)
        temp = arr[k-1]
        arr[k-1] = arr[n-k]
        arr[n-k] = temp

        return arr

    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        arr = []
        count = 0

        while head:
            arr.append(head.val)
            head = head.next
            
        print(arr)
        ans = self.swap(arr , k)

        print(ans)

        anshead = answer =  ListNode(ans[0])

        
        for i in range(1,len(arr)):
            anshead.next = ListNode(arr[i])
            anshead = anshead.next
            

        return answer

            



        

        
            

