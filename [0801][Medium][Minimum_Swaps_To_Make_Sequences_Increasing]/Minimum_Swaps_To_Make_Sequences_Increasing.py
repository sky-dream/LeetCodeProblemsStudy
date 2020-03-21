# leetcode time     cost : 112 ms
# leetcode memory   cost : 13.7 MB 
# Time  Complexity: O(N)
# Space Complexity: O(1)
# solution 1, DP
class Solution(object):
    def minSwap(self, A, B):
        n1, s1 = 0, 1
        for i in range(1, len(A)):
            n2 = s2 = float("inf")
            if A[i-1] < A[i] and B[i-1] < B[i]:
                n2 = min(n2, n1)
                s2 = min(s2, s1 + 1)
            # due to the description says there must be a solution
            if A[i-1] < B[i] and B[i-1] < A[i]:
                n2 = min(n2, s1)
                s2 = min(s2, n1 + 1)
            # copy current to prev, move forward
            n1, s1 = n2, s2

        return min(n1, s1)

def main():
    A = [1,3,5,4]    
    B = [1,2,3,7]      #expect is 1
    obj = Solution()
    res = obj.minSwap(A, B)
    print("return value is ",res);
    
if __name__ =='__main__':
    main()   