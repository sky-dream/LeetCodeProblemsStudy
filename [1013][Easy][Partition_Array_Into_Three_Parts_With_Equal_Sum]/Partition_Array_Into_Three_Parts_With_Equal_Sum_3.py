#solution 1, sum the whole list s, sub list sum is the s//3.
class Solution:
    def canThreePartsEqualSum(self, A) -> bool:
    	S = sum(A)
    	if S % 3 != 0: return False
    	goal, cumulativeSum, partitionCounter = S//3, 0, 0
    	for a in A:
            cumulativeSum += a
            if cumulativeSum == goal:
                if partitionCounter is 2:
                    return True
                cumulativeSum, partitionCounter = 0, partitionCounter+1
    	return False
 
def main():
    array = [0,2,1,-6,6,-7,9,1,2,0,1]      #expect is true   
    obj = Solution()
    res = obj.canThreePartsEqualSum(array)
    print("return value is ",res);
    
if __name__ =='__main__':
    main()  