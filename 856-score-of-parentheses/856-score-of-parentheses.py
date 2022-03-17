class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        
        
        stack = []
		
		# cur: total score so far
		# prev: previous score
        cur, prev = 0, 0
        
        
        # scan each symbol in input S
        for char in S:
            
            if char == '(':
                
                # '(', push in with current socre
                stack.append( cur )
                
                # reset previous and current to zero
                prev, cur = 0, 0
            
            else:
                
                # ')' match with latest '(', get top score
                top = stack.pop()
                
                if prev:
                    # we have valid parenthesis pair inside, add prev
                    cur += top + prev
                else:
                    # no parenthesis pair inside, directly add 1
                    cur += top + 1
            
            # update previous as current
            prev = cur
        
        
        # total score so far
        return cur