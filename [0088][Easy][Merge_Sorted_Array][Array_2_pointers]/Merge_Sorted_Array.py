# leetcode time     cost : 28 ms
# leetcode memory   cost : 13.7 MB 
# Time  Complexity: O((n+m)log(n+m))
# Space Complexity: O(1)
# solution 1, sort, 
class Solution:
    def merge(self, nums1: [int], m: int, nums2: [int], n: int):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[:] = sorted(nums1[:m] + nums2)

def main():
    num1,m,num2,n = [1,2,3,0,0,0],3,[2,5,6],3          
    # expect is [1,2,2,3,5,6],

    obj = Solution()
    obj.merge(num1,m,num2,n)
    result = num1       
    print("return result is ",result);
    
if __name__ =='__main__':
    main() 