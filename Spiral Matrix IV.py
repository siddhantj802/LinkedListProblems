# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:

        # make the matrix
        matrix = [[-1]*n for _ in range(m)]

        # initialize the directions generator
        directions_generator = self.directions_generator()

        # get the first directions
        direction = next(directions_generator)

        # introduce the boundaries
        left = 0
        right = n - 1
        up = 0
        down = m - 1

        # introduce pointer to the current element
        rx = 0
        cx = 0

        # go through the linked list
        while head:

            # get the current value
            val = head.val

            # place it into the matrix
            matrix[rx][cx] = val

            # going right and reached right boundary
            if direction[1] == 1 and cx == right:
                direction = next(directions_generator)
                up += 1
            
            # going down and reached down boundary
            elif direction[0] == 1 and rx == down:
                direction = next(directions_generator)
                right -= 1
            
            # going left and reached left boundary
            elif direction[1] == -1 and cx == left:
                direction = next(directions_generator)
                down -= 1
            
            # going up and reached upper boundary
            elif direction[0] == -1 and rx == up:
                direction = next(directions_generator)
                left += 1
            
            # update the positions
            rx += direction[0]
            cx += direction[1]

            # update list head
            head = head.next
        
        return matrix

    def directions_generator(self):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        pointer = 0
        while True:
            yield directions[pointer]
            pointer = (pointer + 1) % 4
