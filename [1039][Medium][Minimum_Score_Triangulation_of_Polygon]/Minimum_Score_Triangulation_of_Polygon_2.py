# leetcode time     cost : 140 ms
# leetcode memory   cost : 13.7 MB
# Time  Complexity: O(N**3)
# Space Complexity: O(N**2)
# solution 2, Greedy
class Solution:
    def __init__(self):
        self.result=0
    def _find(self,A,m,length):  ###寻找最小边的两个端点，需要处理许多边界情况
        if m == 0:
            n = A[2:-1].index(min(A[2:-1])) + 2
        elif m==1:
            n=A[3:].index(min(A[3:]))+3
        elif m == length - 1:
            n = A[1:-2].index(min(A[1:-2])) + 1
        elif m==length-2:
            n=A.index(min(A[:-3]))
        else:
            minimum=min(min(A[:m - 1]), min(A[m + 2:]))
            n=A[:m-1].index(minimum) if minimum in A[:m-1] else A[m+2:].index(minimum)+m+2
        return (m, n)
    def find_element(self,A):  ###区分一些边界情况，包括两个和三个连续最小值
        length=len(A)
        minimum=min(A)
        if A.count(minimum) == 2:
            for i in range(-1, length - 1):
                if (A[i], A[i + 1]) == (minimum, minimum):
                    y = self._find(A, i + 1, length)
                    i = length - 1 if i == -1 else i
                    x = self._find(A, i, length)
                    return x if A[x[1]] < A[y[1]] else y
            else:
                return self._find(A,A.index(minimum),length)
        elif A.count(minimum)==3:
            for i in range(-2,length-2):
                if (A[i],A[i+1],A[i+2])==(minimum,minimum,minimum):
                    return (i,i+2) if i>0 else (i+2,length+i)
            else:
                return self._find(A,A.index(minimum),length)
        else:
            return self._find(A,A.index(minimum),length)
    def _execute(self,A):
        if len(A)==3:  ##三角形只有一种情况
            self.result+=(A[0]*A[1]*A[2])
        elif len(A)==4: ##四边形只有两种情况
            self.result+=min(A[0]*A[1]*A[2]+A[0]*A[2]*A[3],A[0]*A[1]*A[3]+A[1]*A[2]*A[3])
        else:
            m,n=self.find_element(A)
            a=min(m,n)
            b=max(m,n)
            self._execute(A[a:b+1])  ##分解为两个子多边形
            self._execute(A[:a+1]+A[b:])
    def minScoreTriangulation(self, A) -> int:
        self._execute(A)
        return self.result