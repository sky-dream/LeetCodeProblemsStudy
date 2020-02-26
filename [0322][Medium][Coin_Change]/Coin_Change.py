# leetcode time     cost : 1460  ms
# leetcode memory   cost : 13.7 MB 
# Time  Complexity: O(n*k)
# Space Complexity: O(n)
# slolution 1, Dynamic programming - Bottom up,loop money amount with iteration
class Solution(object):
    # def coinChange(self, coins: List[int], amount: int) -> int:
    def coinChange(self, coins, amount):
        rs = [amount+1] * (amount+1)
        rs[0] = 0
        for i in range(1, amount+1):
            for c in coins:
                if i >= c:
                    rs[i] = min(rs[i], rs[i-c] + 1)

        if rs[amount] == amount+1:
            return -1
        return rs[amount]
# leetcode time     cost : 1012 ms
# leetcode memory   cost : 13.5 MB     
    def coinChange_2(self, coins: 'List[int]', amount: 'int') -> 'int':
            dp = [0] + [float('inf') for i in range(amount)]
            for i in range(1, amount+1):
                for coin in coins:
                    if i - coin >= 0:
                        dp[i] = min(dp[i], dp[i-coin] + 1)
            if dp[-1] == float('inf'):
                return -1
            return dp[-1]