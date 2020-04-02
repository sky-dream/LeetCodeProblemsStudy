# leetcode time     cost : 52 ms
# leetcode memory   cost : 13.6 MB 
# Time  Complexity: O(MN)
# Space Complexity: O(MN)
# solution 1, DP
class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        #dp[i] is the min clips number can cover the time 0-i
        dp =[float('inf')]*(T+1)
        #clips = sorted(clips,key = lambda x:x[0])     # reverse=True降序， 默认升序
        #if (clips[0][0] > 0): 
            #return -1
        dp[0] = 0
        for i in range(1,T+1):
            for clip in clips:
                # 找到包含结束端点的视频片段
                if (clip[0] < i <= clip[1]):
                    # 缩小问题范围，求覆盖 (0 - clip[0]) 区间的视频的最小片段数量 
                    dp[i] = min(dp[i], dp[ clip[0] ] + 1)
        return -1 if (dp[T] == float('inf')) else dp[T]