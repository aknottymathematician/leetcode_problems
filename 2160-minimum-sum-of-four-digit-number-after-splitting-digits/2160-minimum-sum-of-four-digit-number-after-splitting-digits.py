class Solution:
    def minimumSum(self, num: int) -> int:
        sumArr = []
        m = 0
        while num > 0:
            sumArr.append(num%10)
            num = num//10
            # m+=1
        print(sumArr)
        sumArr.sort()
        print(sumArr)
        num1 = sumArr[0]*10 + sumArr[3]
        num2 =sumArr[1]*10 + sumArr[2]
        return num1+num2