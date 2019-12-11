class Solution(object):  
    def __init__(self):
        self.result = []
        self.cols = []
        self.xy_sum = []
        self.xy_diff = [] 

    def DFS(self,n,queens,xy_sum,xy_diff):
        row = len(queens)
        # recursion terminator
        if row == n:
            #print("matched solution found,queens is "+str(queens)+", add the solution in result array.")
            self.result.append(queens)
            return True
        
        for col in range(n):
            if col not in queens and row+col not in xy_sum and row-col not in xy_diff:
                #The queen will not be attacked in this [row][col] position, queen can be put here.
                #print("****************************current level is "+str(row)+", matched col found in current row,"+"row: "+str(row)+", col: "+str(col)+", go deeper level*************************************")
                self.DFS(n,queens + [col], xy_sum + [row+col], xy_diff+[row-col]) 
                #print("****************************current level is "+str(row)+", return back from deeper level*************************************")
        #print("in current level, queens: "+str(queens)+", xy_sum: "+str(xy_sum)+", xy_diff: "+str(xy_diff)+", row: "+str(row)+", col: "+str(col))  
        queens = [];xy_diff = [];xy_sum = [];
        return  False

    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        if n< 1: return self.result       
        self.DFS(n,self.cols,self.xy_sum,self.xy_diff)
        return [["."*i + "Q" + "."*(n-i-1) for i in sol] for sol in self.result]
s = Solution()
print(s.solveNQueens(4))