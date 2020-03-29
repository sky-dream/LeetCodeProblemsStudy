# leetcode time     cost : 360 ms
# leetcode memory   cost : 13.7 MB 
# Time  Complexity: O(N)
# Space Complexity: O(1)
# solution 4 , DP
class Solution:
    def knightDialer(self, N: int) -> int:
        a0 = a1 = a2 = a3 = a4 = a5 = a6 = a7 = a8 = a9 = 1
        for _ in range(N - 1):
            a0, a1, a2, a3, a4, a5, a6, a7, a8, a9 = a4 + a6, a6 + a8, a7 + \
                a9, a4 + a8, a0 + a3 + a9, 0, a0 + a1 + a7, a2 + a6, a1 + a3, a2 + a4
        return (a0 + a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8 + a9) % (10**9 + 7)

def main():
    N = 4551      #expect is 318799568
    obj = Solution()
    res = obj.knightDialer(N)
    print("return value is ",res);
    
if __name__ =='__main__':
    main()    