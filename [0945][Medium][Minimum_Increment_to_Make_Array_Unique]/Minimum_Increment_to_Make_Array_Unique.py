# leetcode time     cost : 668 ms
# leetcode memory   cost : 18.9 MB 
# Time  Complexity: O(L) ,其中 L 的数量级是数组 A 的长度加上其数据范围内的最大值
# Space Complexity: O(L)
# solution 1, brute force
class Solution:
    def minIncrementForUnique(self, A: [int]) -> int:
        count = [0] * 80000
        for x in A:
            count[x] += 1
        
        ans = taken = 0
        for x in range(80000):
            if count[x] >= 2:
                # record repeated num amount(1 individual can keep),
                taken += count[x] - 1
                # save already get value sum of repeat num,used to consist of not appear num value
                ans -= x * (count[x] - 1)
            elif taken > 0 and count[x] == 0:
                # when one not appear num reached, the repeat amount decrease 1.
                taken -= 1
                # use move to change repeat num to not appear num value
                ans += x
        
        return ans

def main():
    array = [3,2,1,2,1,7]      #expect is 6
    obj = Solution()
    res = obj.minIncrementForUnique(array)
    print("return value is ",res);
    
if __name__ =='__main__':
    main()   