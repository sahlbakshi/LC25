# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """

        arr = []
        for head in lists:
            curr = head
            while curr:
                arr.append(curr.val)
                curr = curr.next
        
        arr.sort()
        res = ListNode()
        head = res

        for num in arr:
            res.next = ListNode(num, None)
            res = res.next
        
        return head.next


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """

        def mergeTwoLists(l1, l2):
            head = ListNode()
            node = head

            while l1 and l2:
                if l1.val < l2.val:
                    node.next = l1
                    l1 = l1.next
                else:
                    node.next = l2
                    l2 = l2.next
                node = node.next
            
            if l1:
                node.next = l1
            
            if l2:
                node.next = l2
            
            return head.next   

        
        if len(lists) == 0:
            return None
            
        for i in range(1, len(lists)):
            lists[i] = mergeTwoLists(lists[i-1], lists[i])
        
        return lists[-1]
            