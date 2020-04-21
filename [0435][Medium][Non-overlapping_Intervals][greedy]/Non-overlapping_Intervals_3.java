// leetcode time     cost : 4 ms
// leetcode memory   cost : 39.7 MB
// Time  Complexity: O(nlog(n))
// Space Complexity: O(1)
/// solution 3, greedy, sort by end time
class Solution {
    public int eraseOverlapIntervals(int[][] intervals) {
        if (intervals.length == 0) return 0;
    
        // 按照结束时间将所有区间进行排序
        Arrays.sort(intervals, (i1, i2) -> Integer.compare(i1[1], i2[1]));
        // 定义一个变量 end 用来记录当前的结束时间，count 变量用来记录有多少个没有重叠的区间
        int end = intervals[0][1], count = 1;
        // 从第二个区间开始遍历剩下的区间  
        for (int i = 1; i < intervals.length; i++) {
            // 当前区间和前一个结束时间没有重叠，那么计数加 1，同时更新一下新的结束
            if (intervals[i][0] >= end) {
                end = intervals[i][1];
                count++;
            }
        }
    
        // 用总区间的个数减去没有重叠的区间个数，即为最少要删除掉的区间个数
        return intervals.length - count; 
    }
}