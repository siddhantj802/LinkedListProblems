# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def findend(self,elist):
        temp = elist
        while temp.next:
            temp = temp.next
        return temp
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        
        count = 0

        curr = list1
        strt = curr
        

        while count != a-1 :
            curr = curr.next
            strt = curr

            count += 1

        while count != b+1 :
            curr = curr.next
            count += 1

        end = self.findend(list2)

        strt.next = list2
        end.next = curr

        return list1

        


    


        

        
