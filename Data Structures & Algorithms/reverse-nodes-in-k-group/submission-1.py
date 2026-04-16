# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        head, tail = self.reverseK(head, k)
        while tail:
            next_head, tail = self.reverseK(tail, k)
            head = self.join(head, next_head)
        return head
    
    def join(self, l1, l2):
        head = curr = l1
        while curr.next:
            curr = curr.next
        curr.next = l2
        return l1

    def reverseK(self, head, k):
        count = 0
        tail = head
        while tail:
            count += 1
            tail = tail.next
            if count == k:
                break
        
        if count < k:
            return (head, None)
        
        curr = head
        prev = None
        count = 0
        while count < k:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            count += 1
        return (prev, curr)
