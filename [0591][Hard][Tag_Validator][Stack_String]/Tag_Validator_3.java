// leetcode time     cost : 24 ms
// leetcode memory   cost : 41.4 MB
// Time  Complexity: O(n)
// Space Complexity: O(n)
// https://leetcode.com/problems/tag-validator/discuss/103364/Java-Solution-7-lines-Regular-Expression
// solution 2, Regular-Expression.
/*
Two brilliant points:
1. Use Non Greedy mode (.*?) when matching CDATA. 
   Reference: https://stackoverflow.com/questions/3075130/what-is-the-difference-between-and-regular-expressions
2. Use Group (([A-Z]{1,9}) then \\1) when matching TAG_NAME. 
   Reference: http://www.regular-expressions.info/refcapture.html
*/
public class Solution {
    public boolean isValid(String code) {
        if (code.equals("t")) return false;
        code = code.replaceAll("<!\\[CDATA\\[.*?\\]\\]>", "c");

        String prev = "";
        while (!code.equals(prev)) {
            prev = code;
            code = code.replaceAll("<([A-Z]{1,9})>[^<]*</\\1>", "t");
        }

        return code.equals("t");
    }
}