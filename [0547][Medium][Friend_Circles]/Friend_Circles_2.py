# solution 1 greedy algorithm.
# leetcode time     cost : 216 ms
# leetcode memory   cost : 14.6 MB 
# Time  Complexity: O(n**2)
# Space Complexity: O(1)
# solution 1, DFS,
class Solution:
    def findCircleNum(self, matrix_M):
        N = len(matrix_M)
        visited = set()
        def dfs(node):
            for j, friend_i_j in enumerate(matrix_M[node]):  #dfs(i), nei is col j, adj is the matrix_M[i][j],
                if friend_i_j and (j not in visited):
                    visited.add(j)
                    dfs(j)
        
        ans = 0
        for i in range(N):
            if i not in visited:
                dfs(i)
                ans += 1
        return ans
    
def main():
    M = [[1,1,0],[1,1,0],[0,0,1]]
    obj = Solution()
    res = obj.findCircleNum(M)
    print("return value is ",res)
    
if __name__ =='__main__':
    main()     