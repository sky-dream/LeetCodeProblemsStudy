# solution 2,2 pointers
# leetcode time     cost : 80 ms
# leetcode memory   cost : 13.7 MB 
# Time  Complexity: O(N)
# Space Complexity: O(1)
class Solution:
    def compress(self, chars) -> int:
        anchor = write = 0
        for read, c in enumerate(chars):
            if read + 1 == len(chars) or chars[read + 1] != c:
                chars[write] = chars[anchor]
                write += 1
                if read > anchor:
                    for digit in str(read - anchor + 1):
                        chars[write] = digit
                        write += 1
                anchor = read + 1
                
        n = len(chars)
        for i in range(write,n):
            chars.pop(-1)
        #print(chars)    
        return write
    
def main():
    chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b","c","c","c"]
    obj = Solution()
    res = obj.compress(chars)
    print("return value is "+str(res));
    
if __name__ =='__main__':
    main()     