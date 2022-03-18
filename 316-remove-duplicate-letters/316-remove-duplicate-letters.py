class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_occ = {c: i for i, c in enumerate(s)}
        stack = ["!"]
        visited = set()
        
        for i, symbol in enumerate(s):
            if symbol in visited:
                continue
            while symbol<stack[-1] and last_occ[stack[-1]] > i:
                visited.remove(stack.pop())
                
            stack.append(symbol)
            visited.add(symbol)
            
        return "".join(stack)[1:]