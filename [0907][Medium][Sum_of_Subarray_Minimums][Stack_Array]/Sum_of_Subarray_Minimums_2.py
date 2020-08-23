# Time  Complexity: O(N) 
# Space Complexity: O(N)
# solution 2, 单调栈 Monotone Stack
class Solution(object):
    def sumSubarrayMins(self, A):
        MOD = 10**9 + 7

        stack = []
        ans = dot = 0
        for idx, value in enumerate(A):
            # Add all answers for subarrays [i, idx], i <= idx
            count = 1
            while stack and stack[-1][0] >= value:
                temp_idx, temp_val = stack.pop()
                count += temp_val
                dot -= temp_idx * temp_val

            stack.append((value, count))
            dot += value * count
            ans += dot
        return ans % MOD

def main():
    nums = [3,1,2,4]      #expect is 17
    obidx = Solution()
    res = obidx.sumSubarrayMins(nums)
    print("return value is ",res);
    
if __name__ =='__main__':
    main()   