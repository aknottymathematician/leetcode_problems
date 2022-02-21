class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        memory = {}
        elem = []
        if len(nums) ==1:
            return nums
        for num in nums:
            if num in memory:
                memory[num] = memory.get(num, 0) + 1
            else:
                memory[num] = 1
        for k in memory:
            if memory[k]>len(nums)//3:
                elem.append(k)
        return elem