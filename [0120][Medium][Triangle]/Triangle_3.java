// leetcode time     cost : 2 ms
// leetcode memory   cost : 39.1 MB
// solution 1, DP by iterate from the last 2nd row to the top row.
import java.util.List;
import java.util.Arrays;
import java.util.ArrayList;
import java.math.*;
class Solution {
    public int minimumTotal(List<List<Integer>> triangle) {
        // corner case
        if(triangle == null || triangle.size() == 0) 
            return 0;        
        for(int i=triangle.size()-2;i>=0;i--){
            for(int j=0;j<=i;j++){
                int self = triangle.get(i).get(j);         //get row(i+1)  clo(j+1)
                int res = Math.min(triangle.get(i+1).get(j)+self,   triangle.get(i+1).get(j+1)+self);    //get the sum for this row and below row
                triangle.get(i).set(j,res);         //update row(i+1)  clo(j+1)
            }
        }
        return triangle.get(0).get(0);  //return row(0) clo(0)
    }
}

public class Triangle_3 {
    public static void main(String args[]) {
        int[][] triangle_int = {{2},{3,4},{6,5,7},{4,1,8,3}} ;   // expect is 11
        List<List<Integer>> triangle = new ArrayList<List<Integer>>();
        
         for(int i = 0;i < triangle_int.length;i++){
            // need to new the tmp object in the loop, otherwise the triangle.add(i,tmp) will overwrite all the elements before 
            // due to the tmp reference called in the add function.
            List<Integer> tmp = new ArrayList<Integer>();
            for(int j =0;j <= i;j++){
                tmp.add(j,triangle_int[i][j]);
            }
            triangle.add(i,tmp);
            //System.out.println("i is :"+i+",triangle is :" + triangle+",tmp: "+tmp);
        } 
        Solution Solution_obj = new Solution();
        int result = Solution_obj.minimumTotal(triangle);
        System.out.println("In java code,return value is :" + (result));
    }
}