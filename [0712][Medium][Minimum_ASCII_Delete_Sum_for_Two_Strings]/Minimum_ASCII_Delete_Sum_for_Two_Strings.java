// leetcode time     cost : 40 ms
// leetcode memory   cost : 56 MB 
// Time  Complexity: O(M*N)
// Space Complexity: O(1)
class Solution {
        int[][] dp = new int[1010][1010];    //the max sum of ascii
        char[] s1,s2;
        int minimumDeleteSum(String str1, String str2) {
            str1=' '+str1;
            str2=' '+str2;
            s1= str1.toCharArray(); 
            s2= str2.toCharArray();
            int max_ascii=0,sum_ascii=0;        
            
            for(int i=1;i<s1.length;i++) sum_ascii+=s1[i];
            for(int i=1;i<s2.length;i++) sum_ascii+=s2[i];
    
            for(int i=0;i<s1.length;i++){
                for(int j=0;j<s2.length;j++){
                    if(i==0||j==0){
                        dp[i][j]=0;
                    }
                    else{
                        if(s1[i]==s2[j]) dp[i][j]=dp[i-1][j-1]+s1[i];
                        else dp[i][j]=Math.max(dp[i-1][j],dp[i][j-1]);
                    }
                    max_ascii=Math.max(max_ascii,dp[i][j]);
                }
            }
            return sum_ascii-max_ascii*2;
        }
    };

public class Minimum_ASCII_Delete_Sum_for_Two_Strings {
    public static void main(String args[]) {
        String s1 = "sea";
        String s2 = "eat"; // #expect is 231
        Solution Solution_obj = new Solution();
        int result = Solution_obj.minimumDeleteSum(s1,s2);
        System.out.println("In java code, result is "+ result);
    }
}