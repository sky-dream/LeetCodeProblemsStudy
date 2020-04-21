// leetcode time     cost : 2 ms
// leetcode memory   cost : 40.2 MB
// Time  Complexity: O(log(min(m,n)))
// Space Complexity: O(1)
// solutioin 1, binary search, divide
class Solution {
    public double findMedianSortedArrays(int nums1[], int nums2[]) {
        int m = nums1.length;
        int n = nums2.length;
    
        int k = (m + n) / 2;
    
        if ((m + n) % 2 == 1) {
            return findKth(nums1, 0, m - 1, nums2, 0, n - 1, k + 1);
        } else {
            return (
                findKth(nums1, 0, m - 1, nums2, 0, n - 1, k) + 
                findKth(nums1, 0, m - 1, nums2, 0, n - 1, k + 1)
            ) / 2.0;
        }
    }
    public double findKth(int[] nums1, int l1, int h1, int[] nums2, int l2, int h2, int k){
        int m = h1 - l1 + 1;
        int n = h2 - l2 + 1;
    
        if (m > n) {
            return findKth(nums2, l2, h2, nums1, l1, h1, k);
        }
    
        if (m == 0) {
            return nums2[l2 + k - 1];
        }
    
        if (k == 1) {
            return Math.min(nums1[l1], nums2[l2]);
        }
    
        int na = Math.min(k/2, m);
        int nb = k - na;
        int va = nums1[l1 + na - 1];
        int vb = nums2[l2 + nb - 1];
    
        if (va == vb) {
            return va;
        } else if (va < vb) {
            return findKth(nums1, l1 + na, h1, nums2, l2, l2 + nb - 1, k - na );
        } else {
        return findKth(nums1, l1, l1 + na - 1, nums2, l2 + nb, h2, k - nb );
        }
    
    }
}