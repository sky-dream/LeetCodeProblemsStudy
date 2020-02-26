// leetcode time     cost : 22 ms
// leetcode memory   cost : 41.4 MB 
// Time  Complexity: O(S*n), S is the needed money amount
// Space Complexity: O(S)
// https://leetcode-cn.com/problems/coin-change/solution/ling-qian-dui-huan-by-leetcode/
// slolution 4, Dynamic programming - loop coin with iteration, similar to solution 2,
public class Solution {
    public int coinChange(int[] coins, int amount) {

      if(coins==null || coins.length==0||amount==0) return 0;
        
      if(coins.length==1 && coins[0]>amount) return -1;
      
      if(coins.length==1 && coins[0]==amount) return 1;
        
        int[] arr= new int[amount+1];
        Arrays.fill(arr, amount+1);
        arr[0]=0;
        for(int coin : coins){
            for(int a=coin;a<=amount;a++){
                arr[a]=Math.min(arr[a], arr[a-coin]+1);
            }
        }
        return arr[arr.length-1]>amount?-1:arr[arr.length-1];
        
    }
}