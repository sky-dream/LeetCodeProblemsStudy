# leetcode time     cost : 172 ms
# leetcode memory   cost : 13.7 MB 
# Time  Complexity: O(n)
# Space Complexity: O(n)
# slolution 2, Dynamic programming - Bottom up,loop money amount with recursion
class Solution:
  def coinChange(self, coins: List[int], amount: int) -> int:
    coins.sort(reverse = True)
    min_coins = float('inf')
    
    def count_coins(start_coin, coin_count, remaining_amount):
      nonlocal min_coins
      
      if remaining_amount == 0:
        min_coins = min(min_coins, coin_count)
        return
      
      # Iterate from largest coins to smallest coins
      for i in range(start_coin, len(coins)):
        remaining_coin_allowance = min_coins - coin_count
        max_amount_possible = coins[i] * remaining_coin_allowance
        
        if coins[i] <= remaining_amount and remaining_amount < max_amount_possible:
          count_coins(i, coin_count + 1, remaining_amount - coins[i])
      
    count_coins(0, 0, amount)
    return min_coins if min_coins < float('inf') else -1