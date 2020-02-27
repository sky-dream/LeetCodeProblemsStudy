# solution 1 greedy algorithm.
# leetcode time     cost : 324 ms
# leetcode memory   cost : 29.5 MB 
# Time  Complexity: O(n**2)
# Space Complexity: O(1)
# solution 5, numpy,compute the transitive closure of the (boolean) matrix 
# and count the number of different rows:
import numpy as np
class Solution(object):
    def findCircleNum(self, M):
        return len(set(map(tuple, (np.matrix(M, dtype='bool')**len(M)).A)))
    
def main():
    M = [[1,1,0],[1,1,0],[0,0,1]]
    obj = Solution()
    res = obj.findCircleNum(M)
    print("return value is ",res)
    
if __name__ =='__main__':
    main()     