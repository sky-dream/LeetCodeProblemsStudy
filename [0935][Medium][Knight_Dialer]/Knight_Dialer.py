# leetcode time     cost : --- ms, max time exceeded
# leetcode memory   cost : --- MB 
# Time  Complexity: O(N*12*8) 
# Space Complexity: O(1)
# solution 1, DP
class Solution:
    def knightDialer(self, N: int) -> int:
        directions = [[-2,1],[-2,-1],[2,-1],[2,1],[-1,-2],[1,-2],[-1,2],[1,2]]
        # init the status for num 0-9 to 1,
        dp = dp2 = [[1]*(3) for _ in range(4)]
        # exclude the 2 special point
        dp[3][0] = dp[3][2] = 0    
        max_mod = 10**9 +7
        def isOnBoard(r,c):
            return (0<=r<3 and 0<=c<3) or (r==3 and c==1) 
        if N==1:
            return 10
        for step in range(1,N): 
            dp2 = [[0]*(3) for _ in range(4)]

            for row in range(4):
                for col in range(3):
                    if isOnBoard(row,col):
                        for direct in directions: 
                            new_r = row + direct[0]
                            new_c = col + direct[1]
                            if isOnBoard(new_r,new_c):
                                dp2[new_r][new_c] += dp[row][col]
                                dp2[new_r][new_c]  = dp2[new_r][new_c] %max_mod
            dp = dp2
        res = sum([sum(row) for row in dp2])
        return res%max_mod

def main():
    N = 161      #expect is 533302150
    obj = Solution()
    res = obj.knightDialer(N)
    print("return value is ",res);
    
if __name__ =='__main__':
    main()   