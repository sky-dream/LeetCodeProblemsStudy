# solution 1 greedy algorithm.
# leetcode time     cost : 220 ms
# leetcode memory   cost : 13.8 MB 
# Time  Complexity: O(n**2)
# Space Complexity: O(1)
# solution 3, UnionFind,
class Solution:
    def findCircleNum(self, M):
        def find(node):
            if circles[node] == node: return node
            root = find(circles[node])
            circles[node] = root
            return root
        
        n = len(M)
        circles = {x:x for x in range(n)}
        num = n
        for i in range(n):
            for j in range(i, n):
                if i != j and M[i][j] == 1 and find(i) != find(j):
                    circles[find(i)] = find(j)   
                    
        return sum([1 for k, v in circles.items() if k == v])
    
def main():
    M = [[1,1,0],[1,1,0],[0,0,1]]
    obj = Solution()
    res = obj.findCircleNum(M)
    print("return value is ",res)
    
if __name__ =='__main__':
    main()     