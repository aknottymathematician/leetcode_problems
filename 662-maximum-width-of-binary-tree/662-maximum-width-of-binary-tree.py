# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        Q = collections.deque()
        Q.append((root,0))
        ans = 0
        while Q:
            length = len(Q)
            _, start = Q[0]
            for i in range(length):
                node, index = Q.popleft()
                if node.left:
                    Q.append((node.left, 2*index))
                if node.right:
                    Q.append((node.right, 2*index+1))
            ans = max(ans, index-start+1)
        return ans