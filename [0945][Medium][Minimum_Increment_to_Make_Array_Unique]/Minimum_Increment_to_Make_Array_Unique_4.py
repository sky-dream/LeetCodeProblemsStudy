# leetcode time     cost : 352 ms
# leetcode memory   cost : 18.9 MB 
# Time  Complexity: O(N*logN)
# Space Complexity: O(N)
#solution 4 , sort with counter
class Solution:
    def minIncrementForUnique(self, A: [int]) -> int:
        # counter数组统计每个数字的个数。
        # max used to shorten the loop up bound 
        counter = [0]*40001
        upperBound = -1
        for num in A:
            counter[num]+=1
            upperBound = max(upperBound, num)  
        # 遍历counter数组，若当前数字的个数cnt大于1个，则只留下1个，其他的cnt-1个后移
        move = 0
        for num in range(upperBound+1):
            if (counter[num] > 1):
                d = counter[num] - 1
                move += d
                # 做 d 次move, 把重复dAmount次的元素移到 [num+1] 的位置
                counter[num + 1] += d
        # 最后, counter[upperBound+1]里可能会有从counter[upperBound]后移过来的，
        # counter[max+1]里只留下1个，其它的d个后移。
        # 设 upperBound+1 = x，那么后面的d 个数就是[x+1,x+2,x+3,...,x+d],
        # 因此操作次数是[1,2,3,...,d],用求和公式求和。
        d = counter[upperBound + 1] - 1
        move += (1 + d) * d // 2
        return move

def main():
    array = [3,2,1,2,1,7]      #expect is 6
    obj = Solution()
    res = obj.minIncrementForUnique(array)
    print("return value is ",res)
    
if __name__ =='__main__':
    main()   