# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        queue = deque([root])
        
        if not root:
            return []
        
        while queue:
            level = []
            for i in range(len(queue)):
                curNode = queue.popleft()
                level.append(curNode.val)
                
                if curNode.left: queue.append(curNode.left)
                if curNode.right: queue.append(curNode.right)
                
            result.append(level)
        return result[::-1]