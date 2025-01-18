# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None

        node = ListNode()
        head = node

        curr1 = list1
        curr2 = list2 

        while curr1 and curr2:
            if curr1.val < curr2.val:
                node.val = curr1.val
                curr1 = curr1.next
            else:
                node.val = curr2.val
                curr2 = curr2.next
                
            if curr1 or curr2:
                node.next = ListNode()
                node = node.next
        
        while curr1:
            node.val = curr1.val
            curr1 = curr1.next
            if curr1:
                node.next = ListNode()
                node = node.next

        while curr2:
            node.val = curr2.val
            curr2 = curr2.next
            if curr2:
                node.next = ListNode()
                node = node.next

        return head
    