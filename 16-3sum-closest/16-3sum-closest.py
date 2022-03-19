class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        result = nums[0]+nums[1]+nums[2]
        n = len(nums)
        
        if n == 3:
            return sum(nums)
        
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            start = i+1
            end = n-1
            while start < end:
                curSum = nums[i]+nums[start]+nums[end]
                if curSum == target:
                    return target
                if abs(curSum-target)<abs(result-target):
                    result = curSum
                if curSum < target:
                    start += 1
                else:
                    end -= 1
            
        return result