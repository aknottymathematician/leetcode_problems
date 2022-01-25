class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        res_dict ={}
        
        for num in nums:
            if num in res_dict:
                return True
            else:
                res_dict[num]=1
        
        return False