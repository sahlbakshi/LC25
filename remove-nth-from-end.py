# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        length = 0
        node = head
        while node:
            length += 1
            node = node.next
        
        index = length - n
        
        if index == 0:
            return head.next
            
        prev = None
        node = head
        while node:
            if index == 0:
                prev.next = node.next
                break
            prev = node
            node = node.next
            index -= 1
        
        return head
