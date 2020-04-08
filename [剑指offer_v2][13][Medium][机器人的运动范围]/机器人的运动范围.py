# leetcode time     cost : 68 ms
# leetcode memory   cost : 16.5 MB 
# Time  Complexity: O(M*N)
# Space Complexity: O(M*N)
# solution 1, dfs
class Solution:
    def movingCount(self, m: int, n: int, k: int):
        visited = [[0]*n for _ in range(m)]
        def isValid(row,col,k,m,n):
            inGridRange = (0<= row <m) and ((0<= col <n))
            # known 1 <= n,m <= 100
            inIndexRange = (row%10 + row//10 + col%10 + col//10) <= k
            return inGridRange and inIndexRange
        directions = [[-1,0],[1,0],[0,-1],[0,1]]
        def dfs(row,col,m,n,k):
            if not isValid(row,col,k,m,n) or visited[row][col]:
                return 0
            else:
                ans = 1
                visited[row][col] = 1
                for direct in directions:
                    n_row = row + direct[0]
                    n_col = col + direct[1]
                    ans += dfs(n_row,n_col,m,n,k)
            return ans
        
        return dfs(0,0,m,n,k)

def main():
    m, n, k = 13,15,7          #expect is 36
    Solution_obj = Solution()
    result = Solution_obj.movingCount(m, n, k)
    print("result value is ",result)
    
if __name__ =='__main__':
    main()  