#solution 1, sum the whole list s, sub list sum is the s//3.
class Solution:
    def canThreePartsEqualSum(self, A) -> bool:
        total = sum(A)
        if total % 3 != 0: return False
        count, cumulativeSum, target = 0, 0, total // 3
        for num in A:
            cumulativeSum += num
            if cumulativeSum == target:
                cumulativeSum = 0
                count += 1
        return count >= 3
 
def main():
    array = [0,2,1,-6,6,-7,9,1,2,0,1]      #expect is true   
    obj = Solution()
    res = obj.canThreePartsEqualSum(array)
    print("return value is ",res);
    
if __name__ =='__main__':
    main()  