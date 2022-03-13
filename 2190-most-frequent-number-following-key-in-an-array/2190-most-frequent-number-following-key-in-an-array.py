class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        count = Counter()
        
        for i,n in enumerate(nums):
            if n==key and i<len(nums)-1:
                count[nums[i+1]] += 1
        
        return count.most_common()[0][0]