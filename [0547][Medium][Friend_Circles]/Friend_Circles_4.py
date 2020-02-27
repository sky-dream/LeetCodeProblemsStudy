# solution 1 greedy algorithm.
# leetcode time     cost : 360 ms
# leetcode memory   cost : 38.9 MB 
# Time  Complexity: O(n**2)
# Space Complexity: O(1)
# https://leetcode.com/problems/friend-circles/discuss/101340/Oneliners-%3A-P
# solution 4, using a SciPy function:,
import scipy.sparse
from scipy.sparse.csgraph import connected_components
import numpy as np
class Solution(object):
    def findCircleNum(self, M):
        # The documentation of scipy.io.wavfile clearly states you should pass it a numpy array:
        # convert Matrix M into numpy array.
        np_array = np.array(M)
        return scipy.sparse.csgraph.connected_components(np_array)[0]
    
def main():
    M = [[1,1,0],[1,1,0],[0,0,1]]
    obj = Solution()
    res = obj.findCircleNum(M)
    print("return value is ",res)
    
if __name__ =='__main__':
    main()     