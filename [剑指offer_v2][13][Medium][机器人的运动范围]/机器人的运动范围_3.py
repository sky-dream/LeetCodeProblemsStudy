# leetcode time     cost : 56 ms
# leetcode memory   cost : 14 MB 
# Time  Complexity: O(M*N)
# Space Complexity: O(M*N)
# solution 3, broadcast
def digitsum(n):
    ans = 0
    while n:
        ans += n % 10
        n //= 10
    return ans

class Solution:
    def movingCount(self, m: int, n: int, k: int):
        visited = set([(0, 0)])
        for i in range(m):
            for j in range(n):
                if ((i - 1, j) in vis or (i, j - 1) in visited) and digitsum(i) + digitsum(j) <= k:
                    visited.add((i, j))
        return len(visited)

def main():
    m, n, k = 13,15,7          #expect is 36
    Solution_obj = Solution()
    result = Solution_obj.movingCount(m, n, k)
    print("result value is ",result)
    
if __name__ =='__main__':
    main()  