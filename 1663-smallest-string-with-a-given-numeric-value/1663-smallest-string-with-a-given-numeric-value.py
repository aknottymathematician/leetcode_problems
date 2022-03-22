class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        p = max(0, (26*n - k - 1)//25)
        q = k - 26*n + 25*p + 26
        return "a"*p + chr(96 + q) + "z"*(n-p-1)