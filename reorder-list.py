# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        left = head
        right = slow.next

        slow.next = None

        prev = None
        curr = right
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        right = prev
        
        i = 0
        while left and right:
            if i % 2 == 0:
                temp = left.next
                left.next = right
                left = temp
            else:
                temp = right.next
                right.next = left
                right = temp
            i += 1
        