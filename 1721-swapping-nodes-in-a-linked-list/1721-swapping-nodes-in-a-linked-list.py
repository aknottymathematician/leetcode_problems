# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        l = r = head
        for _ in range(k-1):
            l = l.next
        # Find kth node from right
        # by finding tail node
        tail = l
        while tail.next:
            r, tail = r.next, tail.next
        # Swap values and return
        l.val, r.val = r.val, l.val
        return head