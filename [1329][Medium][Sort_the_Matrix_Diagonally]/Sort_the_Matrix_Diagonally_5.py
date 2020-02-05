# solution 3,
# leetcode time     cost : 68 ms
# leetcode memory   cost : 12 MB
# Time  Complexity: O(mn log(min(m,n))
# Space Complexity: O(min(m,n))
'''
Like solution 1, but more basic, so easier to port to other languages. 
Note how writing the sorted values backwards has two advantages: 
(1) don't need to reset i and j and 
(2) don't have to sort in reverse and pop takes only O(1) time.
'''
class Solution(object):
    def diagonalSort(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(mat), len(mat[0])
        def sort(i, j):
            vals = []
            while i < m and j < n:
                vals.append(mat[i][j])
                i += 1
                j += 1
            vals.sort()
            while i and j:
                j -= 1
                i -= 1
                mat[i][j] = vals.pop()
        for i in range(m): sort(i, 0)
        for j in range(n): sort(0, j)
        return mat