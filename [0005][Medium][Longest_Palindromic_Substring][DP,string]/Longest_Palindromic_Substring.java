// leetcode time     cost : 195 ms
// leetcode memory   cost : 39.2 MB
// Time  Complexity: O(n**2)
// Space Complexity: O(n)

class Solution {
    // solution 1, 最长公共子串
    public String longestPalindrome(String s) {
        if (s.equals(""))
            return "";
        String origin = s;
        String reverse = new StringBuffer(s).reverse().toString();
        int length = s.length();
        int[] arr = new int[length];
        int maxLen = 0;
        int maxEnd = 0;
        // origin="babacdh", reverse="hdcabab"
        for (int i = 0; i < length; i++)
            /**************状态压缩***************************/
            //for (int j = 0; j < length; j++)
            for (int j = length - 1; j >= 0; j--) {
            /**************************************************/
                if (origin.charAt(i) == reverse.charAt(j)) {
                    if (i == 0 || j == 0) {
                        //arr[i][j] = 1;
                        arr[j] = 1;  //此时无需检查前一个字符，最长公共子串只有一个元素，s[i],
                    } else {
                        //arr[i][j] = arr[i-1][j - 1] + 1;
                        arr[j] = arr[j - 1] + 1;   //此时最长公共子串长度+1，但不一定是s中同一段字符
                    }
                /**************状态压缩***************************/
                //之前二维数组，每次用的是不同的列，所以不用置 0 。
                } else {
                    arr[j] = 0;
                }
                /**************************************************/
                if (arr[j] > maxLen) {
                    int beforeReverseIdx = length - 1 - j;
                    //检查s[i-arr[j], i],reverse[j-arr[j], j] 是否为S中同一段字符
                    if (beforeReverseIdx + arr[j] - 1 == i) {
                        maxLen = arr[j]; //验证合法，则更新公共子串长度到回文子串长度
                        maxEnd = i;
                    }

                }
            }
        return s.substring(maxEnd - maxLen + 1, maxEnd + 1);
    }
    //solution 2,DP， 对每一个字符，从小步长开始逐个尝试，
    public String longestPalindrome_2(String s) {
        int n = s.length(), max = 0, start = 0;
        if(n < 2){
            return s;
        }
        //边界情况，只有一个元素，只有两个元素
        boolean[][] record = new int[n][n];
        for(int i = 0; i < n; i++){
            record[i][i] = true;
        }
        for(int step = 1; step < n; step++){
            for(int i = 0 ; i + step < n; i++){
                int j = i + step;
                if(s.charAt(i) == s.charAt(j)){
                    if(step == 1){
                        record[i][j] = true;
                    }
                    else{
                        //default record[i][j] is false
                        record[i][j] = record[i + 1][j - 1];
                    }
                    if(record[i][j] && max < step){
                        max = step;
                        start = i;
                    }
                }
            }
        }
        return s.substring(start, start + step + 1);
    }

}