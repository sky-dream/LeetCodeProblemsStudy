# leetcode time     cost : 1220 ms
# leetcode memory   cost : 13.7 MB 
# Time  Complexity: O(N) 
# Space Complexity: O(1)
# solution 2, DP
class Solution:
    def knightDialer(self, N: int) -> int:
        # dp[num] is the possible path come to position num, init all with 1
        dp = [1]*10
        # moves[num] = [x1,x2,..] is the possible next position that from num jump to,
        # eg: moves[0] = [4,6], from 0 can go to 4 or 6,
        moves = [[4,6],[6,8],[7,9],[4,8],[3,9,0],[],
                     [1,7,0],[2,6],[1,3],[2,4]]
        max_mod = 10**9 + 7
        
        for i in range(N-1):
            dp2 = [0] * 10
            for start,possible_next in enumerate(moves):
                for k in possible_next:
                    dp2[k] += dp[start]
                    dp2[k] %= max_mod
            dp = dp2
        
        # res maybe very big, do mod,
        return sum(dp) % max_mod

def main():
    N = 4551      #expect is 318799568
    obj = Solution()
    res = obj.knightDialer(N)
    print("return value is ",res);
    
if __name__ =='__main__':
    main()   