[121. [Easy] Best Time to Buy and Sell Stock](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/)

[122. [Easy] Best Time to Buy and Sell Stock II](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/)

[309. [Medium] Best Time to Buy and Sell Stock with Cooldown](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/)

[188. [Hard] Best Time to Buy and Sell Stock IV](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iv/)

[714. [Medium] Best Time to Buy and Sell Stock with Transaction Fee](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/)

[123. [Hard] Best Time to Buy and Sell Stock III](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii/)

**Method 1: straightforward algorithm with O(n) time and O(1) space**

For each day, there are 3 possible actions: buy, sell, nothing.
The action nothing can be interpreted at "sell then immediately buy".
So positive changes of prices are profitable.
```python
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(len(prices) - 1):
            max_profit += max(prices[i+1] - prices[i], 0)
        return max_profit
```
**Method 2: DP algorithm with O(n) time and O(1) space**

For each day, there are 3 possible actions: buy, sell, nothing. Let us define
- buy[i] = maxProfit of prices[:i+1] with the action buy at day i,
- sell[i] = maxProfit of prices[:i+1] with the action sell at day i,
- nothing[i] = maxProfit of prices[:i+1] with the action nothing at day i.

The base cases are buy[0] = -prices[0], sell[0] = nothing[0] = 0. The recursive relationships are
- buy[i] = max(max(sell[i-1], nothing[i-1]) - prices[i], buy[i-1]) # no cool down
- sell[i] = max(buy[i-1] + prices[i], sell[i-1])
- nothing[i] = max(sell[i-1], buy[i-1], nothing[i-1]).
```python
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n < 2: 
            return 0
        prev_buy, prev_sell, prev_nothing = -prices[0], 0, 0
        for i in range(1, n):
            buy  = max(max(prev_sell, prev_nothing) - prices[i], prev_buy) 
            sell = max(prev_buy + prices[i], prev_sell)
            nothing = max(prev_sell, prev_buy, prev_nothing)
            prev_buy, prev_sell, prev_nothing = buy, sell, nothing
        return max(sell, nothing)
```
**Method 3: naive DP algorithm with O(n^2) time and O(n) space**

Let dp[i] = maxProfit of prices[:i+1], the base cases and recursive relationship are
- (i) dp[i] = 0 if i <= 0
- (ii) dp[i] = max(dp[i-1], prices[i] - prices[j] + dp[j-1] for j from 0 to i-1)
Because we have two choices at day i: (1) do nothing at day i, (2) maxProfit of prices[:j], buy at day j, sell at day i.

**Solution 3:** bottom-up approach with a table (Time Limit Exceeded, 200 / 201 test cases passed.)
```python
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n < 2: 
            return 0
        dp = [0 for _ in range(n)]
        for i in range(1, n):
            dp[i] = dp[i-1]
            for j in range(i):
                tmp = prices[i] - prices[j]
                tmp += dp[j-1] if j > 0 else 0
                dp[i] = max(dp[i], tmp)
        return dp[n-1]
```
**Solution 4:** top-down approach with memoization (Time Limit Exceeded, 200 / 201 test cases passed.)
```python
    def maxProfit(self, prices: List[int]) -> int:
        def recursive(i):
            if i <= 0:
                return 0
            if i in mp:
                return mp[i]
            max_profit = recursive(i - 1)
            for j in range(i):
                tmp = prices[i] - prices[j] + recursive(j - 1)
                max_profit = max(max_profit, tmp)
            mp[i] = max_profit
            return mp[i]        
        mp = {}
        return recursive(len(prices) - 1)
```
**Method 4: DP algorithm with O(n) time and O(n) space (Beat 27.94%)**

Let dp[i] = maxProfit of prices[:i+1], the base cases and recursive relationship are
- (i) dp[i] = 0 if i <= 0
- (ii) dp[i] = max(dp[i-1], prices[i] - prices[j] + dp[j-1] for j from 0 to i-1)
**We can further use DP to get local_max = - prices[j] + dp[j-1] for j from 0 to i-1.**
```python
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n < 2: 
            return 0
        dp = [0 for _ in range(n)]
        local_max = -prices[0]
        for i in range(1, n):
            dp[i] = max(dp[i-1], prices[i] + local_max)
            local_max = max(local_max, dp[i-1] - prices[i])
        return dp[n-1]
```