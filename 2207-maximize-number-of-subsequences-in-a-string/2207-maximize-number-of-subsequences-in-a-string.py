class Solution:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        ans = count1 = count2 = 0
        
        for s in text:
            # if pattern[0] == pattern[1]:
            #     return count1*(count1+1)//2
            
            if s == pattern[1]:
                ans+=count1
                count2+=1
                
            if s == pattern[0]:
                count1+=1
            
            
        return max(count1,count2)+ans