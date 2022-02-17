class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        odd = []
        even = []
        n = len(nums)
        
        for i in range(n):
            if i%2==0:
                even.append(nums[i])
            else:
                odd.append(nums[i])
        
        even.sort()
        odd.sort(reverse=True)
        
        evenIdx = 0
        oddIdx = 0
        
        for i in range(n):
            if i%2==0:
                nums[i] = even[evenIdx]
                evenIdx += 1
            
            else:
                nums[i] = odd[oddIdx]
                oddIdx += 1
        
        return nums