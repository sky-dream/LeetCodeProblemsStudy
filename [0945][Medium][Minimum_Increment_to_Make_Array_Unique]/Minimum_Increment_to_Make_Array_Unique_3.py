# leetcode time     cost : 560 ms
# leetcode memory   cost : 18.8 MB 
# Time  Complexity: O(N*logN)
# Space Complexity: O(N)
#solution 3 , sort
class Solution:
    def minIncrementForUnique(self, A: [int]) -> int:
        A.sort()
        ans = 0
        for i in range(1, len(A)):
            # best case is the continous increase array, 
            # if current not bigger than prev,increase it to prev+1 by move
            if (A[i] <= A[i - 1]):
                pre = A[i]
                A[i] = A[i - 1] + 1
                ans += A[i] - pre
        return ans

def main():
    array = [3,2,1,2,1,7]      #expect is 6
    obj = Solution()
    res = obj.minIncrementForUnique(array)
    print("return value is ",res)
    
if __name__ =='__main__':
    main()   