# solution 1, back tracking.
# leetcode time     cost : 32 ms, faster than 100%
# leetcode memory   cost : 13.1 MB 
# Time  Complexity: O(1)
# Space Complexity: O(1)
# Bit Manipulation,DFS,python solution
class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        pos,H,V,G=[],[0]*9,[0]*9,[0]*9 #Empty cells'position,horizontal,vertical,grid
        ctoV={str(i):1<<(i-1) for i in range(1,10)} #eg:'4'=>1000
        self.vtoC={1<<(i-1):str(i) for i in range(1,10)} #eg:100=>'3'
        for i,row in enumerate(board):
            for j,c in enumerate(row):
                if c!='.':
                    v = ctoV[c]
                    H[i],V[j],G[i//3*3+j//3] = H[i]|v,V[j]|v,G[i//3*3+j//3]|v
                else:
                    pos+=(i,j),
        #dict {(i,j):[possible vals(bit-identify),count]}    
        posDict={(i,j):[x,self.countOnes(x)] for i,j in pos \
                    for x in [0x1ff & ~(H[i]|V[j]|G[i//3*3+j//3])]} 
        self.slove(board,posDict)

    def countOnes(self,n):
            count=0
            while n:
                count,n = count+1 , n & ~( n& (~n + 1))
            return count

    def slove(self,board,posDict):
        if len(posDict)==0:
            return True
        p = min(posDict.keys(), key= lambda x: posDict[x][1]) #
        candidate=posDict[p][0]
        while candidate:
            v=candidate & (~candidate + 1) #get last '1'
            candidate &= ~v
            tmp=self.updata(board,posDict,p,v) #updata board and posDict
            if self.slove(board,posDict): #slove next position
                return True
            self.recovery(board,posDict,p,v,tmp) #backtrack-->recovery
        return False

    def updata(self,board,posDict,p,v):
        i,j=p[0],p[1]
        board[i][j]=self.vtoC[v]
        tmp=[posDict[p]]
        del posDict[p]
        for key in posDict.keys(): 
            if i == key[0] or j ==key[1] or (i//3,j//3)==(key[0]//3,key[1]//3): #relevant points
                if posDict[key][0]&v: #need modify
                    posDict[key][0]&= ~v
                    posDict[key][1]-= 1
                    tmp+=key,  #Record these points.  
        return tmp

    def recovery(self,board,posDict,p,v,tmp):
        board[p[0]][p[1]]='.'
        posDict[p]=tmp[0]
        for key in tmp[1:]:
            posDict[key][0]|=v 
            posDict[key][1]+=1