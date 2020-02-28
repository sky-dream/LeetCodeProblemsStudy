# solution 1 greedy algorithm.
# leetcode time     cost : 296 ms
# leetcode memory   cost : 13.7 MB 
# Time  Complexity: O(n**2)
# Space Complexity: O(1)
# solution 2, iteration,
class Solution(object):
    def findCircleNum(self, M):
        seen = set([])
        res = 0
        for i in range(len(M)):
            if i not in seen:
                toSee = [i]
                while len(toSee):
                    # pop out the last element, use toSee.pop(0) can pop out the first element
                    cur = toSee.pop()       
                    if cur not in seen:
                        seen.add(cur)
                        toSee = [j for j,value in enumerate(M[cur]) if value and j not in seen] + toSee
                # when check i, and i not in the checked friends circle beforem then it is in a new friend circle.        
                res += 1
        return res
    
def main():
    M = [[1,1,0],[1,1,0],[0,0,1]]
    obj = Solution()
    res = obj.findCircleNum(M)
    print("return value is ",res)
    
if __name__ =='__main__':
    main()     