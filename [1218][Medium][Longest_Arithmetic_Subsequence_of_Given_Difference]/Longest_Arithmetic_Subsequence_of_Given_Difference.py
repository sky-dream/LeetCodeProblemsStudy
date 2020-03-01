# leetcode time     cost : 796 ms
# leetcode memory   cost : 27.2 MB 
from collections import defaultdict
class Solution:
    #def longestSubsequence(self, arr: List[int], difference: int) -> int:
    def longestSubsequence(self, arr, difference):
        # length_dict key is the value in the array, dict value is the subqueue length that include the current value in the array
        length_dict = defaultdict(int)
        result = 0
        for value in arr:
            length_dict[value] = length_dict[value - difference] + 1 
            result = max (result , length_dict[value] )
        return result
    
def main():
    arr, difference = [1,5,7,8,5,3,4,2,1], -2          # Example 3, expect is 4
    obj = Solution()
    result = obj.longestSubsequence(arr, difference)
    print("return result is :",result)
    
if __name__ =='__main__':
    main() 