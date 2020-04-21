// leetcode time     cost : 2 ms
// leetcode memory   cost : 39.3 MB
// Time  Complexity: O(nlog(n))
// Space Complexity: O(1)
// solution 2, greedy, sort by start time
class Solution {
    public int eraseOverlapIntervals(int[][] intervals) {
        if (intervals.length == 0) return 0; 
    
        // 将所有区间按照起始时间排序
        Arrays.sort(intervals, (i1, i2) -> Integer.compare(i1[0], i2[0]));
        // 用一个变量 end 记录当前的最小结束时间点，以及一个 count 变量记录到目前为止删除掉了多少区间
        int end = intervals[0][1], count = 0;
        // 从第二个区间开始，判断一下当前区间和前一个区间的结束时间
        for (int i = 1; i < intervals.length; i++) {
            // 当前区间和前一个区间有重叠，即当前区间的起始时间小于上一个区间的结束时间，
            // end记录下两个结束时间的最小值，把结束时间晚的区间删除，计数加1。
            if (intervals[i][0] < end) {
                end = Math.min(end, intervals[i][1]);
                count++;
            } else {
                end = intervals[i][1];
            }
        }
        // 如果没有发生重叠，根据贪婪法，更新 end 变量为当前区间的结束时间
        return count;
    
    }
}