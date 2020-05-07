// leetcode time     cost : 14 ms
// leetcode memory   cost : 39.8 MB
// solution 2, based on math, problem tag is string.
public class Solution {
    public String mirroring(String s) {
        String x = s.substring(0, (s.length()) / 2);
        return x + (s.length() % 2 == 1 ? s.charAt(s.length() / 2) : "") + new StringBuilder(x).reverse().toString();
    }
    public String nearestPalindromic(String n) {
        if (n.equals("1"))
            return "0";
        //'200345'---->'200002'
        String a = mirroring(n);
        long diff1 = Long.MAX_VALUE;
        diff1 = Math.abs(Long.parseLong(n) - Long.parseLong(a));
        if (diff1 == 0)
            diff1 = Long.MAX_VALUE;

        StringBuilder s = new StringBuilder(n);
        int i = (s.length() - 1) / 2;
        //'200345'---->'199345'
        //'199345'---->'199991'
        while (i >= 0 && s.charAt(i) == '0') {
            s.replace(i, i + 1, "9");
            //replace(int start, int end, String str),
            //使用给定 String 中的字符替换此序列的子字符串中的字符
            i--;
        }
        if (i == 0 && s.charAt(i) == '1') {
            //public delete(int start, int end),移除此序列的子字符串中的字符
            s.delete(0, 1);
            int mid = (s.length() - 1) / 2;
            s.replace(mid, mid + 1, "9");
        } else
            s.replace(i, i + 1, "" + (char)(s.charAt(i) - 1));
        //'200345'---->'199345'---->'99345'---->'99399'
        //'199345'---->'198345'---->'198891'
        String b = mirroring(s.toString());
        long diff2 = Math.abs(Long.parseLong(n) - Long.parseLong(b));


        s = new StringBuilder(n);
        i = (s.length() - 1) / 2;
        while (i >= 0 && s.charAt(i) == '9') {
            s.replace(i, i + 1, "0");
            i--;
        }
        if (i < 0) {
            s.insert(0, "1");
        } else
            s.replace(i, i + 1, "" + (char)(s.charAt(i) + 1));
        //'199345'---->'200345'---->'200002'
        //'200345'---->'200002'
        String c = mirroring(s.toString());
        long diff3 = Math.abs(Long.parseLong(n) - Long.parseLong(c));

        if (diff2 <= diff1 && diff2 <= diff3)
            return b;
        if (diff1 <= diff3 && diff1 <= diff2)
            return a;
        else
            return c;
    }
}