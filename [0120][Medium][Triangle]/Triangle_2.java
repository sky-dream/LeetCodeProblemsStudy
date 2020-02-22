// leetcode time     cost : 2 ms
// leetcode memory   cost : 39.1 MB
// solution 1, DP by iterate from the last 2nd row to the top row.
import java.util.List;
import java.util.Arrays;
import java.util.ArrayList;
import java.math.*;
class Solution {
    public int minimumTotal(List<List<Integer>> triangle) {
        int row = triangle.size();
        int[] minlen = new int[row+1];
        for (int level = row-1;level>=0;level--){
            for (int i = 0;i<=level;i++){   //row i has (i+1)  numbers
                minlen[i] = Math.min(minlen[i], minlen[i+1]) + triangle.get(level).get(i);
            }
        }
        return minlen[0];
    }
}

public class Triangle_2 {
    public static void main(String args[]) {
        int[][] triangle_int = {{2},{3,4},{6,5,7},{4,1,8,3}} ;   // expect is 11

        Integer[][] triangle_integer = new Integer[triangle_int.length][triangle_int.length];
         for(int i = 0;i < triangle_int.length;i++){
             for(int j =0;j <= i;j++){
                triangle_integer[i][j] = triangle_int[i][j];
             }
        }
        List<List<Integer>> triangle = new ArrayList<List<Integer>>();

        for(int i = 0;i < triangle_int.length;i++){
            triangle.add((List<Integer>)Arrays.asList(triangle_integer[i]));
            //for (int j = 0;j <= i;j++){
                //System.out.println("triangle[i][j] is :" + (triangle.get(i).get(j).toString()));
            //}
        }  
        
        Solution Solution_obj = new Solution();
        int result = Solution_obj.minimumTotal(triangle);
        System.out.println("In java code,return value is :" + (result));
    }
}