# leetcode time     cost : 40 ms
# leetcode memory   cost : 13.6 MB 
# Time  Complexity: O(N)
# Space Complexity: O(1)
class Solution:
    # @param num, a list of integer
    # @return an integer
    def rob(self, num):
        max_3_house_before, max_2_house_before, adjacent = 0, 0, 0
        for cur in num:
            max_3_house_before, max_2_house_before, adjacent = \
            max_2_house_before, adjacent, max(max_3_house_before+cur, max_2_house_before+cur)
        return max(max_2_house_before, adjacent)

def main():
    array = [2,3,2]      #expect is 3   
    obj = Solution()
    res = obj.rob(array)
    print("return value is ",res);
    
if __name__ =='__main__':
    main() 