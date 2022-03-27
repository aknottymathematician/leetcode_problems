class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        return [j for _, j in sorted([(sum(row), ind) for ind, row in enumerate(mat)])[:k]]