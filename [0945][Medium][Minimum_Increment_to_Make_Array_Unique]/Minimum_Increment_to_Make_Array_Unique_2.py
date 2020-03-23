# leetcode time     cost : 396 ms
# leetcode memory   cost : 18.6 MB 
# Time  Complexity: O(N*logN)
# Space Complexity: O(N)
#solution 2 , sort
class Solution:
    def minIncrementForUnique(self, A: [int]) -> int:
        A.sort()
        A.append(100000)
        ans = taken = 0

        for i in range(1, len(A)):
            if A[i-1] == A[i]:
                taken += 1
                # save already get value sum of repeat num,used to consist of not appear num value
                ans -= A[i]
            else:
                # the max can change to value is the min of repeat num amount and the num amount in [[A[i−1]+1,A[i]−1]]
                give = min(taken, A[i] - A[i-1] - 1)
                # add the delta num value sum of the num we changed to
                ans += give * (give + 1) // 2 + give * A[i-1]
                # remove already change repeat num
                taken -= give

        return ans

def main():
    array = [3,2,1,2,1,7]      #expect is 6
    obj = Solution()
    res = obj.minIncrementForUnique(array)
    print("return value is ",res);
    
if __name__ =='__main__':
    main()   