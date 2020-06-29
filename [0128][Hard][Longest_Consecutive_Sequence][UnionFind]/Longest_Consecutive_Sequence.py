# solution 1, DP,UnionFind
# leetcode time     cost : 44 ms
# leetcode memory   cost : 14.8 MB 
# Time  Complexity: O(N)
# Space Complexity: O(N)
class Solution(object):
    def longestConsecutive(self, nums):
        hash_dict = dict()
        
        max_length = 0
        for num in nums:
            if num not in hash_dict:
                left = hash_dict.get(num - 1, 0)
                right = hash_dict.get(num + 1, 0)
                
                cur_length = 1 + left + right
                if cur_length > max_length:
                    max_length = cur_length
                
                hash_dict[num] = cur_length
                hash_dict[num - left] = cur_length
                hash_dict[num + right] = cur_length
        return max_length

def main():
    inputX,expectRes = [100, 4, 200, 1, 3, 2], 4
    obj = Solution()
    result = obj.longestConsecutive(inputX)
    try:
        assert result == expectRes
        print("passed, result is follow expect:",result)
    except AssertionError as aError:
        print('failed, result >> ', result,"<< is wrong, ","expect is : "+ expectRes)
    
if __name__ =='__main__':
    main()  