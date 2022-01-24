# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        sorted_array = []
        self.inOrderTraversal(root, sorted_array)
        return sorted_array[k-1]
    
    def inOrderTraversal(self, node, sorted_array):
        if node == None:
            return
        
        self.inOrderTraversal(node.left, sorted_array)
        sorted_array.append(node.val)
        self.inOrderTraversal(node.right, sorted_array)
        
        return sorted_array