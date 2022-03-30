class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def search(lo, hi):
            if lo > hi: return False
            mid = (lo + hi) // 2
            curr = matrix[mid // len(matrix[0])][mid % len(matrix[0])]
            if target > curr: return search(mid + 1, hi)
            if target < curr: return search(lo, mid - 1)
            return True
        return search(0, len(matrix[0]) * len(matrix) - 1)