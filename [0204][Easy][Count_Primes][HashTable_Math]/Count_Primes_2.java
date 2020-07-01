// leetcode time     cost : 16 ms
// leetcode memory   cost : 38.4 MB
// solution 2, Sieve of Eratosthenes
// https://leetcode-cn.com/problems/count-primes/solution/ru-he-gao-xiao-pan-ding-shai-xuan-su-shu-by-labula/
import java.util.Arrays;
class Solution {
    int countPrimes(int n) {
        boolean[] isPrim = new boolean[n];
        Arrays.fill(isPrim, true);
        for (int i = 2; i * i < n; i++) 
            if (isPrim[i]) 
                for (int j = i * i; j < n; j += i) 
                    isPrim[j] = false;
        
        int count = 0;
        for (int i = 2; i < n; i++)
            if (isPrim[i]) count++;
        
        return count;
    }
}

public class Count_Primes_2 {
    public static void main(String args[]) {
        int num = 10;   // expect is 4
        Solution Solution_obj = new Solution();
        int result = Solution_obj.countPrimes(num);
        System.out.println("In java code,return value is :" + (result));
    }
}