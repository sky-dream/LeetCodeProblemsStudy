# leetcode time     cost : 500 ms
# leetcode memory   cost : 37 MB 
# Time  Complexity: O(N)
# Space Complexity: O(N)
#solution 5 , linear probing,线性探测法,开放定址法,open addressing,
class Solution:
    def minIncrementForUnique(self, A: [int]) -> int:
        pos = [-1]*80000        # -1表示空位
        move = 0
        def findPos(a):
            b = pos[a]
            # 如果a对应的位置pos[a]是空位，直接放入即可。
            if (b == -1): 
                pos[a] = a
                return a
            # 否则向后寻址
            # 因为pos[a]中标记了上次寻址得到的空位，因此从pos[a]+1开始寻址就行了（不需要从a+1开始）。
            b = findPos(b + 1) 
            pos[a] = b # 寻址后的新空位要重新赋值给pos[a]哦，路径压缩就是体现在这里。
            return b 
        
        # 遍历每个数字a对其寻地址得到位置b, b比a的增量就是操作数。
        for a in A:
            b = findPos(a) 
            move += (b - a)
        return move  

def main():
    array = [3,2,1,2,1,7]      #expect is 6
    obj = Solution()
    res = obj.minIncrementForUnique(array)
    print("return value is ",res)
    
if __name__ =='__main__':
    main()   