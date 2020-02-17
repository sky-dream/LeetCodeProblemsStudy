// solution 3, bit op and recursion,
// leetcode time     cost : 1 ms
// leetcode memory   cost : 39.9 MB 
// Time  Complexity: O(logN)
// Space Complexity: O(logN)
class Solution {
  public int mySqrt(int x) {
    if (x < 2) return x;

    int left = mySqrt(x >> 2) << 1;
    int right = left + 1;
    return (long)right * right > x ? left : right;
  }
}