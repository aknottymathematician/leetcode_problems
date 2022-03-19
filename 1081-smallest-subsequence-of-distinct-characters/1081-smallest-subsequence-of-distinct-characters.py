class Solution:
    def smallestSubsequence(self, s: str) -> str:
        lastOcc = {c: i for i,c in enumerate(s)}
        stack = []
        visited = set()
        
        
        for i, symbol in enumerate(s):
            if symbol in visited:
                continue
            while stack and symbol<stack[-1] and lastOcc[stack[-1]] > i:
                visited.remove(stack.pop())
            
            stack.append(symbol)
            visited.add(symbol)
        return "".join(stack)