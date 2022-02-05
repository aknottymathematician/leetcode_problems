class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        setTable={}
        for i in arr:
            if 2*i in setTable or i/2 in setTable:
                return True
            if i not in setTable:
                setTable[i]=None
        return False