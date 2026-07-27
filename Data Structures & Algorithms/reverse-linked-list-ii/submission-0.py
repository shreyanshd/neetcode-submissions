# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        
        leftPrev = dummy
        for _ in range(left - 1):
            leftPrev = leftPrev.next

        sublist_head = leftPrev.next
        sublist_tail = sublist_head
        for _ in range(right - left):
            sublist_tail = sublist_tail.next
        
        rightNext = sublist_tail.next
        sublist_tail.next = None

        reversed_sublist = self.reverse(sublist_head)

        leftPrev.next = reversed_sublist
        sublist_head.next = rightNext

        return dummy.next


    def reverse(self, head):
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
