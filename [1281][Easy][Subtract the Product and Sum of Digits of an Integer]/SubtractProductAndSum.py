class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        multi_value = 1
        sum_value = 0
        while n:            
            multi_value  = (n%10) *multi_value
            sum_value =  (n%10)  +sum_value
            n = n/10
        return (multi_value - sum_value)