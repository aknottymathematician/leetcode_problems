"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        #base case
        if not head:
            return None
        
        #add add new nodes to dictionary using old nodes as values
        d = {}
        prev, cur = None, head
        while cur:
            d[cur] = copy.copy(cur)
            
            #set next pointers
            if prev:
                d[prev].next = d[cur]
            
            prev, cur =cur, cur.next
            
        #set random pointers using dictionary
        cur = head
        while cur:
            if cur.random:
                d[cur].random = d[cur.random]
            cur = cur.next
        
        #return
        return d[head]