# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head

        if not fast or not fast.next:
            return

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None

        list1 = head
        list2 = self.reverseList(slow)

        dummy = node = ListNode()
        while list1 and list2:
            node.next = list1
            list1 = list1.next
            node = node.next
            node.next = list2
            list2 = list2.next
            node = node.next
        
        node = list1 or list2
        head = dummy.next

    def reverseList(self, head: Optional[ListNode]):
        curr = head
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev


