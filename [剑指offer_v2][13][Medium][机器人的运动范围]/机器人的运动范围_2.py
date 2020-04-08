# leetcode time     cost : 140 ms
# leetcode memory   cost : 14 MB 
# Time  Complexity: O(M*N)
# Space Complexity: O(M*N)
# solution 2,BFS
def digitsum(n):
    ans = 0
    while n:
        ans += n % 10
        n //= 10
    return ans

class Solution:
    def movingCount(self, m: int, n: int, k: int):
        from queue import Queue
        q = Queue()
        q.put((0, 0))
        s = set()
        while not q.empty():
            x, y = q.get()
            if (x, y) not in s and 0 <= x < m and 0 <= y < n and digitsum(x) + digitsum(y) <= k:
                s.add((x, y))
                for nx, ny in [(x + 1, y), (x, y + 1)]:
                    q.put((nx, ny))
        return len(s)

def main():
    m, n, k = 13,15,7          #expect is 36
    Solution_obj = Solution()
    result = Solution_obj.movingCount(m, n, k)
    print("result value is ",result)
    
if __name__ =='__main__':
    main()  