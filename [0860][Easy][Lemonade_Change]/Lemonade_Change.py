# solution 1 greedy algorithm.
# leetcode time     cost : 136 ms
# leetcode memory   cost : 12.1 MB 
# Time  Complexity: O(N)
# Space Complexity: O(1)
class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        five = ten = 0
        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                if not five: return False
                five -= 1
                ten += 1
            else:
                if ten and five:
                    ten -= 1
                    five -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
        return True
    
def main():
    bills = [5,5,10,20]
    obj = Solution()
    res = obj.lemonadeChange(bills)
    print("return value is "+str(res));
    
if __name__ =='__main__':
    main()     