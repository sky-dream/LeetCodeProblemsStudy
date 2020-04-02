# leetcode time     cost : 36 ms
# leetcode memory   cost : 13.7 MB 
# Time  Complexity: O(MN)
# Space Complexity: O(MN)
# solution 2, greedy
class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        n = len(clips)
        clips = sorted(clips,key = lambda x:x[0])     # reverse=True降序， 默认升序
        res = last_end = j = 0
        for i in range(n):
            if last_end >= T: break
            maxLength = last_end 
            while (j < n and clips[j][0] <= last_end):  #  贪心地寻找能够overlap的区间中找最长的
                maxLength = max(maxLength, clips[j][1])
                j+=1
            if (j == i): return -1  # 找不到可选区间
            last_end = maxLength
            i = j - 1
            res += 1 
        return -1 if last_end < T else res