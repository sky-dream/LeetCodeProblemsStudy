// leetcode time     cost : 52 ms
// leetcode memory   cost : 16.5 MB 
// Time  Complexity: O(S*n), S is the needed money amount
// Space Complexity: O(S)
// https://leetcode.com/problems/coin-change/discuss/77373/6-7-lines-2-ways
// slolution 1, coins outer loop, average 92ms
#include <vector>
#include <iostream>
using namespace std;
class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        //new a vector need[amount+1] and init all its elements to the max value amount+1.
        // need[amount+1] is the smallest Num of coins when the need money is amount.
        vector<int> need(amount+1, amount+1);
        need[0] = 0;
        for (int coin : coins)
            for (int amount_x=coin; amount_x<=amount; amount_x++){
                need[amount_x] = min(need[amount_x], need[amount_x-coin] + 1);
                cout << "amount_x: "<< amount_x<<",need[amount_x] value is " << (need[amount_x])<< '\n';
            }
        return need.back() > amount ? -1 : need.back();
    }
};

int main(){
    vector<int> coins = {1, 2, 5};   // expect is 3, 11 = 5 + 5 + 1
    int amount = 11;
    Solution *Solution_obj = new Solution();
    int result = Solution_obj->coinChange(coins, amount);
	  cout << "In cpp code,result value is " << (result)<< '\n';
    return 0;
}