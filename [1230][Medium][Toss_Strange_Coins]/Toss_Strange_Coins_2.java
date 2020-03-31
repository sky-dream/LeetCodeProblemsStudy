// leetcode time     cost : 9 ms
// leetcode memory   cost : 53.3 MB 
// Time  Complexity: O(MN)
// Space Complexity: O(1)
// solution 1, DP, refer to No.322
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
        double []dp = new double[target+1];
        dp[0] = 1-prob[0];
        dp[1] = prob[0];
        for(int i=1;i<prob.length;i++)
        {
            for(int j=target;j>=0;j--)
            {
                if(j>i+1)
                    continue;
                dp[j] = dp[j]*(1-prob[i]);
                if(j-1>=0)
                dp[j]+=dp[j-1]*prob[i];
            }
        }
        return dp[target];
    }
}
