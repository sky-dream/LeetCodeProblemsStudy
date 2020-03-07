// leetcode time     cost : 1177 ms
// leetcode memory   cost : 41 MB
// solution 1, brute force
public class Solution {
   public int largestRectangleArea(final int[] heights) {
       int maxarea = 0;
       for (int i = 0; i < heights.length; i++) {
           for (int j = i; j < heights.length; j++) {
               int minheight = Integer.MAX_VALUE;
               for (int k = i; k <= j; k++)
                   minheight = Math.min(minheight, heights[k]);
               maxarea = Math.max(maxarea, minheight * (j - i + 1));
           }
       }
       return maxarea;
   }
}