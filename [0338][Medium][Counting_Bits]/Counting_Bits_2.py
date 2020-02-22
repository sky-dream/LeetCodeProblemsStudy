# leetcode time     cost : 48 ms
# leetcode memory   cost : 14.5 MB 
# Time  Complexity: O(n)
# Space Complexity: O(n)
# slolution 2, DP and highest effective bit,
# P(i+b)=P(i)+1, b=2**m > i
class Solution:
    def countBits(self, num: int) -> List[int]:
        result = [0 for i in range(num+1)]
        i, b = 0,1
        # [0, b) is calculated
        while (b <= num):
            # generate [b, 2b) or [b, num) from [0, b)
            while(i < b and (i + b) <= num):
                # calculate [1, 2),[2, 4),[4, 8),[8, 16),[16, 32),[32, 64),[64, 128)
                result[i + b] = result[i] + 1
                i+=1
            i = 0    # reset i
            # calculate [0, 1),[0, 2),[0, 4),[0, 8),[0, 16),[0, 32),[0, 64)
            b <<= 1  # b = 2b
        return result