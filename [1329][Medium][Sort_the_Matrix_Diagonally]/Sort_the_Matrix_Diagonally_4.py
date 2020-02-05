# solution 2,
# leetcode time     cost : 76 ms
# leetcode memory   cost : 12.1 MB
# Time  Complexity: O(mn log(min(m,n))
# Space Complexity: O(m*n)
'''
Collect all diagonals, sort them, then write them back. 
By sorting each diagonal in reverse, we can use pop to get the next value in O(1) time.
'''
class Solution(object):
    def diagonalSort(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        # use a special dict,key is i-j, value is diagonal value list,
        # {0: [3, 2, 1], 1: [2, 1], 2: [1], -1: [3, 1, 2], -3: [1], -2: [1, 2]}
        diags = collections.defaultdict(list)
        for i, row in enumerate(mat):
            for j, value in enumerate(row):
                diags[i-j].append(value)      
        for diag in diags.values():
            diag.sort(reverse=True)
        for i, row in enumerate(mat):
            for j, _ in enumerate(row):
                mat[i][j] = diags[i-j].pop()
        return mat