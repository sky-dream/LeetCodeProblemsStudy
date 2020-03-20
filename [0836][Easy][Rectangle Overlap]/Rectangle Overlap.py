# leetcode time     cost : 32 ms
# leetcode memory   cost : 13.5 MB 
# Time  Complexity: O(1)
# Space Complexity: O(1)
# solution 1
class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        return not (rec1[2] <= rec2[0] or  # left
                    rec1[3] <= rec2[1] or  # bottom
                    rec1[0] >= rec2[2] or  # right
                    rec1[1] >= rec2[3])    # top
    
def main():
    rec1 = [0,0,2,2]
    rec2 = [1,1,3,3]         #  true
    obj = Solution()
    res = obj.isRectangleOverlap(rec1, rec2)
    print("return value is "+str(res));
    
if __name__ =='__main__':
    main()     