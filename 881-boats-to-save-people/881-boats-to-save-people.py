class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        start = 0
        end = len(people)-1
        ans = 0
        while start <= end:
            if people[start]+people[end]<=limit:
                start+=1
            end-=1
            ans += 1
            
        return ans