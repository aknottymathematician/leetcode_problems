# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root == None:
            return root
        if root.val == val:
            return root
        def helper(root, val):
            if root == None:
                return root
            if root.val > val:
                return helper(root.left, val)
            if root.val < val:
                return helper(root.right, val)
            if root.val == val:
                return root
        return helper(root, val)