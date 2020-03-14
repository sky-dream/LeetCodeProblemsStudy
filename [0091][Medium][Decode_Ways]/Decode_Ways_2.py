# -*- coding: utf-8 -*-  
# leetcode time     cost : 44 ms
# leetcode memory   cost : 13.5 MB
# https://leetcode.com/problems/decode-ways/discuss/30379/1-liner-O(1)-space
from functools import reduce
class Solution:
    def numDecodings(self, s):
        v, w, p = 0, int(s>''), ''
        for d in s:
            v, w, p = w, (d>'0')*w + (9<int(p+d)<27)*v, d
        return w
    # reduce(function, iterable[, initializer])
    #def numDecodings_2(self, s):
        #return reduce(lambda(v,w,p),d:(w,(d>'0')*w+(9<int(p+d)<27)*v,d),s,(0,s>'',''))[1]*1 

    def numDecodings_3(self, s):
        previous_number_of_ways=0
        number_of_ways=int(s>'')
        previous_digit=''
        
        for digit in s:
            copy_previous=previous_number_of_ways
            previous_number_of_ways=number_of_ways

            #check if the current digit is greater than zero
            #If it is, then (digit>'0') becomes true, and we multiply that by the total number of ways so far
            #...Think permutations
            number_of_ways=(digit>'0')*number_of_ways
            
            #At the same time, we check if the current digit and the next digit, are less than 27..
            #If they are, then its another permutation possibility
            #Again, we are checking the truth, and multiplying it by the number of previously known was, not
            #the current number of ways
            #We have the 9< check because if the digit we are on is a zero, then we won't count the 
            #next permutation
            number_of_ways+= (9<int(previous_digit+digit)<27)*copy_previous

            #Finally, remember that our last digit was the digit we are on now
            previous_digit=digit
            
        return number_of_ways  

def main():
    code = "226"             #expect is 3
    obj = Solution()
    result = obj.numDecodings(code)
    print("return result is :",result)
    
if __name__ =='__main__':
    main()   