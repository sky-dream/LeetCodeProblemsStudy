class Solution(object):  
    def __init__(self):
        self.result = []
        self.cols_position = []
    
    def _getBitPosition(self,PowerOfTwo,n):
        left = 0
        right = n
        while left <= right:
            mid = int((right + left)/2)
            if 2**mid == PowerOfTwo:
                return mid
            if 2**mid < PowerOfTwo:
                left = mid +1
            if 2**mid > PowerOfTwo:
                right = mid -1                         

    def DFS(self,n,row,cols,xy_sum,xy_diff):
        # recursion terminator
        if  row>= n:
            self.result.append(self.cols_position)          
            return True
        #get the available cell in col where can put the queen,start from the lowest bit,
        #only use the n bits integer, use ((1<<n) - 1) as a filter,if n=4, ((1<<n) - 1) = B(1111),
        bits = (~(cols | xy_sum | xy_diff)) & ((1<<n) - 1)
        while bits:
            #use x&(-x) to get the lowest bit of x.
            lowestBitOfAvailableCol = bits & -bits
            col = self._getBitPosition(lowestBitOfAvailableCol,n)
            self.cols_position.append(col)
            #use x<<1 to get the location y=x(x-y=c) that queen maybe attacked,
            #use x>>1 to get the location y=-x(x+y=c) that queen maybe attacked,
            self.DFS(n,row+1,(cols | lowestBitOfAvailableCol),(xy_sum | lowestBitOfAvailableCol ) >>1,(xy_diff | lowestBitOfAvailableCol) <<1)            
            #use x&(x-1) to remove the lowest bit of x.
            bits = bits & (bits - 1)
            #status reverse,remove the element added in current recursion level.only need to remove last element, not reset the whole list.
            self.cols_position = self.cols_position[0:-1]              
        return  False

    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        if n< 1: return self.result       
        self.DFS(n,0,0,0,0)
        return [["."*i + "Q" + "."*(n-i-1) for i in sol] for sol in self.result]    
s = Solution()
print(s.solveNQueens(5))