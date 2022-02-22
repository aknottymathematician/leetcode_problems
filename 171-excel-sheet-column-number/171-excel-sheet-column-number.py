class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        value = []
        print(columnTitle[-1])
        while len(columnTitle) > 0:
            value.append(ord(columnTitle[-1])%32)
            columnTitle=columnTitle[:-1]
        print(value)
        count = 0
        for i in range(len(value)):
            count += (26**i)*value[i]
            
        return count