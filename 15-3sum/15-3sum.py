class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        final_nums = []
        for i in range(len(nums)-2):
            currNum = nums[i]
            left = i+1
            right = len(nums)-1
            
            while left < right:
                currSum = currNum + nums[left] + nums[right]
                if currSum == 0:
                    final_nums.append([currNum, nums[left], nums[right]])
                    left += 1
                    right -= 1
                elif currSum < 0:
                    left += 1
                else:
                    right -= 1
        temp_nums = []
        [temp_nums.append(num) for num in final_nums if not num in temp_nums]
        return temp_nums