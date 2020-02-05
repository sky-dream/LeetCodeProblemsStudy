# solution 1,
# leetcode time     cost : 64 ms
# leetcode memory   cost : 12.1 MB
# Time  Complexity: O(mn log(min(m,n))
# Space Complexity: O(min(m,n))
'''
Optimized version, don't zip i-indexes and j-indexes but rows and j-indexes (still O(min(m,n)) space, 
as mat[i:] only copies references to the rows, not their contents):
'''
class Solution(object):
    def diagonalSort(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(mat), len(mat[0])
        def sort(i, j):
            rj = zip(mat[i:], range(j, n))
            vals = iter(sorted(row[j] for row, j in rj))
            for row, j in rj:
                row[j] = next(vals)
        for i in range(m): sort(i, 0)
        for j in range(n): sort(0, j)
        return mat