class Solution:
    def smallestNumber(self, num: int) -> int:
        numStr = str(num)
        pos = [] 
        neg = []
        if num == 0:
            return num
        
        if numStr[0] == "-":
            for s in numStr:
                if s != "-":
                    neg.append(s)
            neg.sort(reverse=True)
            # for s in neg:
                # if neg[0] == '0':
                #     temp = neg[0]
                #     neg[0] = neg[1]
                #     neg[1] = temp
                #     return +int("-" + "".join(neg))
                # else:
            return int("-" + "".join(neg))            
        else:
            for s in numStr:
                pos.append(s)
            pos.sort()
            
            i=0
            while pos[i] == '0' and i < len(pos):
                i+=1
            temp = pos[0]
            pos[0] = pos[i]
            pos[i] = temp
                    
            return int("".join(pos))

                    