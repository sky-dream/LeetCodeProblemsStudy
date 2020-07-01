// leetcode time     cost : 703 ms
// leetcode memory   cost : 36.4 MB
// solution 1, 
class Solution {
    int countPrimes(int n) {
        int count = 0;
        for (int i = 2; i < n; i++)
            if (this.isPrime(i)) count++;
        return count;
    }
    // 判断整数 n 是否是素数
    boolean isPrime(int n) {
        for (int i = 2; i*i <= n; i++)
            if (n % i == 0)
                // 有其他整除因子
                return false;
        return true;
    }
}

public class Count_Primes {
    public static void main(String args[]) {
        int num = 10;   // expect is 4
        Solution Solution_obj = new Solution();
        int result = Solution_obj.countPrimes(num);
        System.out.println("In java code,return value is :" + (result));
    }
}