// leetcode time     cost : 6 ms
// leetcode memory   cost : 40.8 MB
// solution 1, DP by iterate from the last 2nd row to the top row.
import java.util.List;
import java.util.LinkedList;
import java.util.ArrayList;
import java.util.Deque;
import java.math.*;
class Solution {
    public int minimumTotal(List<List<Integer>> triangle) {
        Deque<Integer> queue = new LinkedList<Integer>();
        int count=triangle.size();
        queue.add(triangle.get(0).get(0));
        for (int i=1;i<count;i++){
            List<Integer> list= triangle.get(i);
            for (int j=0;j<=i;j++){
                int min=0;
                if (j==0)
                     min=list.get(0)+queue.peekFirst();               	
                else if (j==i)
                     min =list.get(j)+queue.pollFirst();              	
                else
                    min = Math.min(queue.pollFirst(),queue.peekFirst())+list.get(j);              	               
                queue.addLast(min);               
            }
        }
        int result=Integer.MAX_VALUE;
        for (int i=0;i<count;i++)
            result=Math.min(result, queue.pollFirst());
        return result;
    }
}

public class Triangle_4 {
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