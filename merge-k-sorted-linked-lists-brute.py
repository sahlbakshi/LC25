# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nodes = []
        for each in lists:
            node = each
            while node:
                nodes.append(node)
                node = node.next
        
        nodes.sort(key=lambda x: x.val)

        head = ListNode()
        curr = head
        for node in nodes:
            curr.next = node
            curr = curr.next 
            node = node.next

        return head.next
