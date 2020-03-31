// leetcode time     cost : 19 ms
// leetcode memory   cost : 49.2 MB 
// Time  Complexity: O(MN)
// Space Complexity: O(MN)
// solution 1, DP, refer to 0-1 knapack
class Solution {
    public double probabilityOfHeads(double[] prob, int target) {
        /*
        dp[i,target]代表抛掷前i个硬币，正面超上的硬币数等于target的概率
        当前投出target可以是（1）当前没投出正面，前i-1个投出target（2）当前投出正面，前i-1个投出target-1
        dp[i,target] = dp[i-1,target-1]*prob[i]+dp[i-1,target]*(1-prob[i])
        */
        double result = 1;
        //如果target=0
        if(target==0){ 
            for(double coin:prob)
                result = result*(1-coin);
            return result;
        }
        int N = prob.length;
        double [][]dp = new double[N][target+1];
        dp[0][0] = 1-prob[0];
        dp[0][1] = prob[0];
        for(int i=1;i<prob.length;i++)
        {
            for(int j=0;j<=target;j++)
            {
                //不能让当前prob中可用的硬币数（i+1）小于j（正面超上的硬币数）
                if(i+1<j)
                    break;
                dp[i][j] = dp[i-1][j]*(1-prob[i]);
                if(j-1>=0)
                dp[i][j]+=dp[i-1][j-1]*prob[i];
            }
        }
        return dp[N-1][target];
    }
}