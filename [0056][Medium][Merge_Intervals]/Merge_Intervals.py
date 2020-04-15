# -*- coding: utf-8 -*-  
# leetcode time     cost : 52 ms
# leetcode memory   cost : 14.5 MB
# Time  Complexity: O(nlogn)
# Space Complexity: O(logn)
# solution 1, sort
class Solution:
    def merge(self, intervals: [[int]]):
        intervals.sort(key=lambda x: x[0])

        merged = []
        for interval in intervals:
            # 如果列表为空，或者当前区间与上一区间不重合，直接添加
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # 否则的话，我们就可以与上一区间进行合并
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged

def main():
    intervals = [[1,3],[2,6],[8,10],[15,18]]   
    expect = [[1,6],[8,10],[15,18]]
    obj = Solution()
    result = obj.merge(intervals)
    try:
        assert result == expect
        print("passed, result is follow expectation:",result)
    except AssertionError as aError:
        print('failed, result is wrong',result, aError.__str__())
    
if __name__ =='__main__':
    main()   