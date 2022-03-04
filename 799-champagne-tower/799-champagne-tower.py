class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        if poured==0:
            return 0
        glasses = [poured]
        # row 1 is filled with inital value, hence start from row 2
        # since the input is 0 indexed, we need to go till (query row + 1 ) + 1 = query row + 2
        for i in range(2,query_row+2):
            #initialize the next row glasses in temp
            temp = [0]*i
            for j in range(len(glasses)):
                # anything excess 1, overflow the current row to next row.  
                if (glasses[j]-1)/2 > 0:
                    # overflow will equally split into right and left.
                    # 0th glass will flow into 0 and 1 glass in next row , 1->(1,2) 2->(2,3) 3->(3,4) etc
                    temp[j] += (glasses[j]-1)/2
                    temp[j+1] += (glasses[j]-1)/2
            glasses = temp
        #incase if the row has still something to overflow, we should return 1 hence the min function below   
        return min(1,glasses[query_glass])
                
# Time Complexity: First loop -> number of rows, second loop -> number of rows, Hence O(N^2)     