class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashnums = {}
        for i, num in enumerate(nums):
            pot_num = target-nums[i]
            if pot_num in hashnums:
                return [i, hashnums[pot_num]]
            else:
                hashnums[num]=i
        return []