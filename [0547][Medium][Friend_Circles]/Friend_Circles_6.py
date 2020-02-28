# solution 1 greedy algorithm.
# leetcode time     cost : 240 ms
# leetcode memory   cost : 13.7 MB 
# Time  Complexity: O(n**2)
# Space Complexity: O(1)
# solution 3, Easy Python Union Find
class Solution(object):
    def findCircleNum(self, M):
        def find(x):
            if x != parents[x]:
                parents[x] = find(parents[x])
            return parents[x]    
        def union(x, y):
            parents[find(x)] = find(y)
            
        n = len(M)
        parents = list(range(n))
        for i in range(len(M)):
            for j in range(len(M[i])):
                if M[i][j]:
                    union(i, j)
        #circle = set(find(i) for i in range(n))            
        #return len(circle) 
        return sum(1 for i in range(n) if i==parents[i])
    
def main():
    M = [[1,1,0],[1,1,0],[0,0,1]]
    obj = Solution()
    res = obj.findCircleNum(M)
    print("return value is ",res)
    
if __name__ =='__main__':
    main()     