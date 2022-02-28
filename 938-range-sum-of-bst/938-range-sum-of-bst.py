# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def inOrder(node):
            if not node:
                return None
            inOrder(node.left)
            self.Tsum+=node.val if low<=node.val<=high else 0
            inOrder(node.right)
        self.Tsum = 0
        inOrder(root)
        return self.Tsum