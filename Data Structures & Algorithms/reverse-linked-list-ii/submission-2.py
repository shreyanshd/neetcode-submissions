# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # create a dummy node
        dummy = ListNode()
        dummy.next = head
        
        # save leftPrev - the node just before sublist starts
        leftPrev = dummy
        for _ in range(left - 1):
            leftPrev = leftPrev.next

        # find the head and tail of sublist to be reversed
        sublist_head = leftPrev.next
        sublist_tail = sublist_head
        for _ in range(right - left):
            sublist_tail = sublist_tail.next
        
        # save rightNext - the node just after sublist ends
        # cut the sublist 
        rightNext = sublist_tail.next
        sublist_tail.next = None

        # reverse the sublist
        reversed_sublist_head, reversed_sublist_tail = self.reverse(sublist_head)

        # fix the pointers - leftPrev and rightNext to the reversed sublist
        leftPrev.next = reversed_sublist_head
        reversed_sublist_tail.next = rightNext

        # return head
        return dummy.next

    """
    Reverses a linked list and returns (head, tail)
    """
    def reverse(self, head):
        tail = head
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev, tail
