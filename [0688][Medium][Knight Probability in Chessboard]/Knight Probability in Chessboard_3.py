# leetcode time     cost : 253 ms
# leetcode memory   cost : 13.8 MB 
# Time  Complexity: O(N*N*K)
# Space Complexity: O(N*N)
# solution 2, DP, use dict to record the possible after every step
class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        p = {(r, c): 1}
        for _ in range(K):
            p = {(r, c): sum(p.get((r+i, c+j), 0) + p.get((r+j, c+i), 0) for i in (1, -1) for j in (2, -2)) / 8 
                 for r in range(N) for c in range(N)}
        
        return sum(p.values())

def main():
    N, K, r, c = 8,5,6,4 #expect is 0.241851806640625
    obj = Solution()
    result = obj.knightProbability(N, K, r, c)
    print("return result is ",result);

if __name__ =='__main__':
    main() 