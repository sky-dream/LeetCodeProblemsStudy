# leetcode time     cost : 44 ms
# leetcode memory   cost : 13.7 MB 
# Time  Complexity: O(m+n)
# Space Complexity: O(m)
# solution 2, 2 pointers, from start to the end 
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Make a copy of nums1.
        nums1_copy = nums1[:m] 
        nums1[:] = []

        # Two get pointers for nums1_copy and nums2.
        p1 = 0 
        p2 = 0
        
        # Compare elements from nums1_copy and nums2
        # and add the smallest one into nums1.
        while p1 < m and p2 < n: 
            if nums1_copy[p1] < nums2[p2]: 
                nums1.append(nums1_copy[p1])
                p1 += 1
            else:
                nums1.append(nums2[p2])
                p2 += 1

        # if there are still elements to add
        if p1 < m: 
            nums1[p1 + p2:] = nums1_copy[p1:]
        if p2 < n:
            nums1[p1 + p2:] = nums2[p2:]

def main():
    num1,m,num2,n = [1,2,3,0,0,0],3,[2,5,6],3          
    # expect is [1,2,2,3,5,6],

    obj = Solution()
    obj.merge(num1,m,num2,n)
    result = num1       
    print("return result is ",result);
    
if __name__ =='__main__':
    main() 