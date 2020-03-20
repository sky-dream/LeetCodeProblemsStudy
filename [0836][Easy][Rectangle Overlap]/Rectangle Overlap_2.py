# leetcode time     cost : 36 ms
# leetcode memory   cost : 13.4 MB 
# Time  Complexity: O(1)
# Space Complexity: O(1)
# solution 2
class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        def intersect(p_left, p_right, q_left, q_right):
            return min(p_right, q_right) > max(p_left, q_left)
            
        return (intersect(rec1[0], rec1[2], rec2[0], rec2[2]) and
                intersect(rec1[1], rec1[3], rec2[1], rec2[3]))
    
def main():
    rec1 = [0,0,2,2]
    rec2 = [1,1,3,3]         #  true
    obj = Solution()
    res = obj.isRectangleOverlap(rec1, rec2)
    print("return value is "+str(res));
    
if __name__ =='__main__':
    main()     