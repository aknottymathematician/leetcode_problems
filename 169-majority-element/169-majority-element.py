class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        memory, counter = 0, 0
        
        for num in nums:
            if counter == 0:
                memory = num
                counter += 1
            elif memory == num:
                counter+=1
            else:
                counter-=1
        return memory