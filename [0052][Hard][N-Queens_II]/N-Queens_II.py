class Solution(object):  
    def __init__(self):
        self.count = 0                    

    def DFS(self,n,row,cols,xy_sum,xy_diff):
        # recursion terminator
        if  row>= n:
            self.count =self.count + 1
            return True
        #get the available cell in col where can put the queen,start from the lowest bit,
        #only use the n bits integer, use ((1<<n) - 1) as a filter,if n=4, ((1<<n) - 1) = B(1111),
        bits = (~(cols | xy_sum | xy_diff)) & ((1<<n) - 1)
        while bits:
            #use x&(-x) to get the lowest bit of x.
            lowestBitOfAvailableCol = bits & -bits
            #use x<<1 to get the location y=x(x-y=c) that queen maybe attacked,
            #use x>>1 to get the location y=-x(x+y=c) that queen maybe attacked,
            self.DFS(n,row+1,(cols | lowestBitOfAvailableCol),(xy_sum | lowestBitOfAvailableCol ) >>1,(xy_diff | lowestBitOfAvailableCol) <<1)
            #use x&(x-1) to remove the lowest bit of x.
            bits = bits & (bits - 1)             
        return  False

    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        if n< 1: return self.count       
        self.DFS(n,0,0,0,0)
        return self.count   
s = Solution()
print(s.totalNQueens(6))