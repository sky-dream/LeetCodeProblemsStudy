class Solution(object):
    def __init__(self):
        self.result = []
        self.cols = set()
        self.pie = set()
        self.na = set()        

    def DFS(self,n,row,current_state):
        # recursion terminator
        if row >= n:
            self.result.append(current_state)
            return
        
        for col in range(n):
            if col in self.cols or row+col in self.pie or row-col in self.na:
                #The queen will be attacked in this [row][col] position, queen should not be put here.
                continue
            # update the attacked position flag
            self.cols.add(col)
            self.pie.add(row+col)
            self.na.add(row-col)
            # go to deeper recursion level, check the next row, add the valid col position into current_state
            self.DFS(n,row+1,current_state+[col])
            # reset the flag variables that used in current level
            self.cols.remove(col)
            self.pie.remove(row+col)
            self.na.remove(row-col)

    def _generate_result(self,n):
        board = []
        for  res in self.result:
            for i in res:
                board.append("."*i+"Q"+"."*(n-i-1))
        return [board[i:i+n] for i in range(0,len(board),n)]       

    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        if n< 1: return []
        self.DFS(n,0,[])
        return self._generate_result(n)