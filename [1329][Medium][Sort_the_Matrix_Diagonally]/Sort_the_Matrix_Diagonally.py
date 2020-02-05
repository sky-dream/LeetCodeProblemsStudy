# solution 1,
# leetcode time     cost : 124 ms
# leetcode memory   cost : 12.1 MB
# Time  Complexity: O(mn log(min(m,n))
# Space Complexity: O(min(m,n))
'''
For each left cell and each top cell, sort the diagonal starting there. For each diagonal, first compute the list of its index pairs ij. 
Then use that list both for reading the values and for writing them back (after having sorted them).
'''
class Solution(object):
    def diagonalSort(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(mat), len(mat[0])
        def sort(i, j):
            ij = zip(range(i, m), range(j, n))
            vals = iter(sorted(mat[i][j] for i, j in ij))
            for i, j in ij:
                mat[i][j] = next(vals)
        for i in range(m): sort(i, 0)
        for j in range(n): sort(0, j)
        return mat