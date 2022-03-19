class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        sums = []
        n= len(nums)
        
        for i in range(n):
            if i>0 and nums[i]==nums[i-1]:
                continue
            
            start = i+1
            end = n-1
            target = -nums[i]
            
            while start<end:
                if nums[start]+nums[end] == target:
                    sums.append((nums[i], nums[start], nums[end]))
                    start += 1
                    end -= 1
                elif nums[start]+nums[end] < target:
                    start += 1
                
                else:
                    end -= 1
        return set(sums)