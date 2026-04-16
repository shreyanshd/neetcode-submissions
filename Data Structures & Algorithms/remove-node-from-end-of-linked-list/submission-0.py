# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        node = head
        while node:
            count += 1
            node = node.next
        k = count - n

        if k == 0:
            return head.next
        
        node = head
        for i in range(1, k):
            node = node.next
        
        if (node.next):
            node.next = node.next.next
        
        return head