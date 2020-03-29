# leetcode time     cost : 356 ms
# leetcode memory   cost : 13.6 MB 
# Time  Complexity: O(N*N*K)
# Space Complexity: O(N*N)
# solution 2, DP
# dp_raw[r][c][step] is the possible after step move still on the pos (r,c)
# use dp[r][c] as dp_raw[r][c][step-1],dp2[r][c] as dp_raw[r][c][step] to compress dp_raw to 2D
class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        directions = [[-2,1],[-2,-1],[2,-1],[2,1],[-1,-2],[1,-2],[-1,2],[1,2]]
        dp = dp2 = [[0]*(N) for _ in range(N)]
        dp[r][c] = 1    # init the input point
        def isOnBoard(r,c):
            return 0<=r<N and 0<=c<N
        for step in range(K): 
            dp2 = [[0]*(N) for _ in range(N)] 
            for row in range(N):
                for col in range(N):
                    for direct in directions: 
                        new_r = row + direct[0]
                        new_c = col + direct[1]
                        if isOnBoard(new_r,new_c):
                            dp2[new_r][new_c] += dp[row][col]/8
            dp = dp2

        return sum([sum(row) for row in dp2])

def main():
    N, K, r, c = 8,5,6,4 #expect is 0.241851806640625
    obj = Solution()
    result = obj.knightProbability(N, K, r, c)
    print("return result is ",result);

if __name__ =='__main__':
    main() 