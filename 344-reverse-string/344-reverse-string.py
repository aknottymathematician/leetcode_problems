class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s[:] = s[::-1]
#         n = len(s)
        
#         if n == 1:
#             return s
        
#         return self.reverseString(s[:n//2]) + self.reverseString(s[n//2:])