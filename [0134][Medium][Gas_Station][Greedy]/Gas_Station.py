# -*- coding: utf-8 -*-  
# leetcode time     cost : 44 ms
# leetcode memory   cost : 14.3 MB
# Time  Complexity: O(N)
# Space Complexity: O(1)

# solution 1, analysis, Greedy
class Solution:
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        n = len(gas)
        
        total_tank, curr_tank = 0, 0
        starting_station = 0
        for i in range(n):
            total_tank += gas[i] - cost[i]
            curr_tank += gas[i] - cost[i]
            # If one couldn't get here,
            if curr_tank < 0:
                # Pick up the next station as the starting one.
                starting_station = i + 1
                # Start with an empty tank.
                curr_tank = 0
        
        return starting_station if total_tank >= 0 else -1

def main():
    gas, cost = [1,2,3,4,5],[3,4,5,1,2]             #expect is 3
    obj = Solution()
    result = obj.canCompleteCircuit(gas, cost)
    print("return result is :",result)
    
if __name__ =='__main__':
    main() 