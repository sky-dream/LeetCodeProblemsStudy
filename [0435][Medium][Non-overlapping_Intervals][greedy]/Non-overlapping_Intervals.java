// leetcode time     cost : ------- ms
// leetcode memory   cost : -------- MB
// Time  Complexity: O(2**n)
// Space Complexity: O(n)
// solution 1, brute force
class Solution {
    // 在主体函数里，先将区间按照起始时间的先后顺序排序，然后调用递归函数
    public int eraseOverlapIntervals(int[][] intervals) {
        Arrays.sort(intervals, (i1, i2) -> Integer.compare(i1[0], i2[0]));
        return eraseOverlapIntervals(-1, 0, intervals);
    }
    // 递归函数里，先检查是否已经处理完所有的区间，是，表明不需要删除操作，直接返回
    int eraseOverlapIntervals(int prev, int curr, int[][] intervals) {
        if (curr == intervals.length) {
            return 0;
        }
        int taken = Integer.MAX_VALUE, nottaken;
        if (prev == -1 || intervals[prev][1] <= intervals[curr][0]) {
            // 只有当prev, curr没有发生重叠的时候，才可以选择保留当前的区间curr
            taken = eraseOverlapIntervals(curr, curr + 1, intervals);
        }
        // 其他情况，可以考虑删除掉curr区间，看看删除了它之后会不会产生最好的结果
        nottaken = eraseOverlapIntervals(prev, curr + 1, intervals) + 1;
    
        return Math.min(taken, nottaken);
    }
}