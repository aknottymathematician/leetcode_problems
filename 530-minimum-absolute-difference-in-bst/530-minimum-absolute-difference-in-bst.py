# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        def inOrder(root):
            if not root:
                return 0
            elements = []
            if root.left:
                elements += inOrder(root.left)
            elements.append(root.val)
            if root.right:
                elements += inOrder(root.right)
            
            return elements
        ele = inOrder(root)
        curMin = float('inf')
        for i in range(len(ele)-1):
            curMin = min(abs(ele[i] - ele[i+1]), curMin)
        return curMin