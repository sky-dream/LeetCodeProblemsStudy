# leetcode time     cost : 52 ms
# leetcode memory   cost : 14 MB 
# Time  Complexity: O(M*N)
# Space Complexity: O(M*N)
# solution 2,  bfs
class Solution:
    def movingCount(self, m: int, n: int, k: int):
        queue, visited,  = [(0, 0, 0, 0)], set()
        while queue:
            i, j, sum_i, sum_j = queue.pop(0)
            if i >= m or j >= n or k < sum_i + sum_j or (i, j) in visited: continue
            visited.add((i,j))
            # if (x+1)%10 == 0, then sum_(x+1) = sum_x -8,------->19,20--->10,2,
            # if (x+1)%10 != 0, then sum_(x+1) = sum_x +1,------->1,2--->1,2,
            queue.append((i + 1, j, sum_i + 1 if (i + 1) % 10 else sum_i - 8, sum_j))
            queue.append((i, j + 1, sum_i, sum_j + 1 if (j + 1) % 10 else sum_j - 8))
        return len(visited)

def main():
    m, n, k = 13,15,7          #expect is 36
    Solution_obj = Solution()
    result = Solution_obj.movingCount(m, n, k)
    print("result value is ",result)
    
if __name__ =='__main__':
    main()  