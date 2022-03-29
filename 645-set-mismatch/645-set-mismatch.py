class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        return [sum(nums)-sum(set(nums)), (n*(n+1)//2)-sum(set(nums))]