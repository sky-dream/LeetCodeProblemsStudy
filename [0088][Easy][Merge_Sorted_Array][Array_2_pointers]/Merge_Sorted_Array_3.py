# leetcode time     cost : 44 ms
# leetcode memory   cost : 13.5 MB 
# Time  Complexity: O(m+n)
# Space Complexity: O(m)
# solution 3, 2 pointers, from the end to start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # two get pointers for nums1 and nums2
        p1 = m - 1
        p2 = n - 1
        # set pointer for nums1
        p = m + n - 1
        
        # while there are still elements to compare
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] < nums2[p2]:
                nums1[p] = nums2[p2]
                p2 -= 1
            else:
                nums1[p] =  nums1[p1]
                p1 -= 1
            p -= 1
        
        # add missing elements from nums2
        nums1[:p2 + 1] = nums2[:p2 + 1]

def main():
    num1,m,num2,n = [1,2,3,0,0,0],3,[2,5,6],3          
    # expect is [1,2,2,3,5,6],

    obj = Solution()
    obj.merge(num1,m,num2,n)
    result = num1       
    print("return result is ",result);
    
if __name__ =='__main__':
    main() 