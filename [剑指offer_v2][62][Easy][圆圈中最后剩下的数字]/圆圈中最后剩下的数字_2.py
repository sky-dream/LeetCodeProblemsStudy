# leetcode time     cost : 2404 ms
# leetcode memory   cost : 17.3 MB 
# Time  Complexity: O(N)
# Space Complexity: O(1)
# solution 3, simulate the operation
class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        i, a = 0, list(range(n))
        while len(a)>1:
            i = (i+m-1)%len(a)
            a.pop(i)
        return a[0]

def main():
    n, m = 5,9          #expect is 1
    Solution_obj = Solution()
    result = Solution_obj.lastRemaining(n, m)
    print("result value is ",result)
    
if __name__ =='__main__':
    main()  