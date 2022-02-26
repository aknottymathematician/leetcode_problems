class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashSum = {}
        
        for i, n in enumerate(nums):
            pot_sum = (target-nums[i])
            
            if pot_sum in hashSum:
                return [i, hashSum[pot_sum]]
            
            else:
                hashSum[n] = i
        return []