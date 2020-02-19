// solution 4, Integer Newton, pls refer to No.69
// leetcode time     cost : 0 ms
// leetcode memory   cost : 36.4 MB 
// Time  Complexity: O(logN)
// Space Complexity: O(1)
class Solution {
  public boolean isPerfectSquare(int num) {
    if (num < 2) return true;

    long x = num / 2;
    while (x * x > num) {
      x = (x + num / x) / 2;
    }
    return (x * x == num);
  }
}