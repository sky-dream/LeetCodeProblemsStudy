#solution 1, sum the whole list s, sub list sum is the s//3. 1 line solution
import itertools
class Solution:
    def canThreePartsEqualSum(self, A: [int]) -> bool:
        # position of sum(A)/3 ought to be ahead of sum(A)*2/3. 
        # This is inherently guaranteed by the fact that accumulate(A) is a generator as x in y is checked first in the generator 
        # and 2*x in y is checked in the remaining generator when x in y is found
    	return (lambda x,y: x in y and 2*x in y)(sum(A)//3,itertools.accumulate(A))
 
 def main():
    array = [0,2,1,-6,6,-7,9,1,2,0,1]      #expect is true   
    obj = Solution()
    res = obj.canThreePartsEqualSum(array)
    print("return value is ",res);
    
if __name__ =='__main__':
    main() 