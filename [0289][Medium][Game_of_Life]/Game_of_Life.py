#-*- coding: utf-8 -*-  
# leetcode time     cost : 48 ms
# leetcode memory   cost : 13.7 MB
# Time  Complexity: O(N*M)
# Space Complexity: O(1)
# solution 1, loop
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)  # row
        m = len(board[0]) # col
        # for current 0, next action die is -2, revive is -3,
        # for current 0, next action die is 2, keep alive is 3,
        # define 8 directions
        directions = [[-1,0],[-1,-1],[0,-1],[1,-1],[1,0],[1,1],[0,1],[-1,1]]
        def isValid(i,j):
            return 0<=i<n and 0<=j<m
        for i in range(n):
            for j in range(m):
                countAlive = 0
                for direct in directions:
                    new_i = i+ direct[0]
                    new_j = j+ direct[1]
                    # count around cell alive
                    if isValid(new_i,new_j) and board[new_i][new_j]>0:
                        countAlive += 1
                # set next action
                if board[i][j] and (countAlive < 2 or countAlive >3):
                    board[i][j] = 2 
                if board[i][j] and (countAlive is 2 or countAlive is 3):
                    board[i][j] = 3
                if board[i][j]==0 and countAlive is 3:
                    board[i][j] = -3
        #print(board)
        for i in range(n):
            for j in range(m):
                board[i][j] = 1 if (board[i][j]==1 or board[i][j]==3 or board[i][j]==-3) else 0