# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        # elements = []
        def inorder(root, elements):
            if root.left:
                inorder(root.left, elements)
            elements.append(root.val)
            if root.right:
                inorder(root.right, elements)
            return elements
        ele = inorder(root, [])
        
        return ele == sorted(ele) and len(ele)==len(set(ele))