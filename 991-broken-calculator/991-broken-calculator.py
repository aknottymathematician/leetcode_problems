class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        if startValue == target:
            return 0
        elif startValue > target:
            return startValue-target
        else:
            if target%2==0:
                return 1 + self.brokenCalc(startValue, target//2)
            elif target %2 ==1:
                return 1 + self.brokenCalc(startValue, target+1)