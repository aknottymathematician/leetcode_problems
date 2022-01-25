# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while root:
            pdiff = root.val - p.val
            qdiff = root.val - q.val
            
            if pdiff > 0 and qdiff > 0:
                root = root.left
                
            elif pdiff < 0 and qdiff < 0:
                root = root.right
            
            else:
                return root