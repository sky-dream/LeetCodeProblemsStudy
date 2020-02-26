# leetcode time     cost : 328 ms
# leetcode memory   cost : 13.6 MB 
# Time  Complexity: O(n)
# Space Complexity: O(n)
# slolution 2, Dynamic programming - Bottom up,loop money amount with Iterative DFS,
class Solution:
    def coinChange(self, coins, amount):
        coins.sort()
        stack = [(0, 0, len(coins))] # steps, accumulated
        min_steps = float('inf')
        while len(stack) != 0:
            steps, accumulated, sequence = stack.pop()
            if accumulated == amount:
                min_steps = min(min_steps, steps)
            if accumulated > amount or amount - accumulated > coins[sequence-1] * (min_steps-steps):
                continue
            for seq, coin in enumerate(coins[:sequence]):
                stack.append((steps+1, accumulated+coin, seq+1))
        return min_steps if min_steps != float('inf') else -1