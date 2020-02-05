# solution 1,
# leetcode time     cost : 64 ms
# leetcode memory   cost : 12.1 MB
# Time  Complexity: O(mn log(min(m,n))
# Space Complexity: O(min(m,n))
'''
solution 1 with nested loops and no helper function.
Note about that j-loop: In the first row, j goes through the whole row, but in lower rows it only goes on the the first cell.
'''
class Solution(object):
    def diagonalSort(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(mat), len(mat[0])
        for i in range(m):
            #combine the sort(i,0) and sort(0,j) with 2 nested loop and below if condition judgement.
            for j in range(1 if i else n):
                rj = zip(mat[i:], range(j, n))
                vals = iter(sorted(r[j] for r, j in rj))
                for r, j in rj:
                    r[j] = next(vals)
        return mat