# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        
        cur = head
        count = 1
        while cur.next:
            count+=1
            cur = cur.next
        cur.next = head
        n = count - (k%count)
        while n >0:
            cur = cur.next
            n-=1
        
        newhead = cur.next
        cur.next = None
        return newhead