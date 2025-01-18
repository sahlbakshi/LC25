# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node_len = 0
        node = head
        while node:
            node_len += 1
            node = node.next

        i = node_len - n
        if i == 0:
            return head.next

        j = 0
        node = head
        while node and node.next:
            if i == j + 1:
                node.next = node.next.next
                break
            j += 1
            node = node.next
        
        return head
        