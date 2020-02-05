# solution 3, based on the greedy,
"""
Imagine that there are two columns needed to be filled: even-indexed and odd-indexed column,
fill the most common chars into the even-indexed column if possible,
fill the remaining chars into the even-indexed column, then odd-indexed column.
"""
# leetcode time     cost : 20 ms
# leetcode memory   cost : 11.8 MB 
import collections
class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        count = collections.Counter(S)
        c_max, f_max = count.most_common(1)[0]
        if 2 * f_max - 1 > len(S):
            return ''
        count.pop(c_max)
        res = len(S) * ['']
        res[:2*f_max:2] = f_max * [c_max]
        i = 2 * f_max
        for c in count:
            for _ in range(count[c]):
                if i >= len(S):
                    i = 1
                res[i] = c
                i += 2
        return ''.join(res)

def main():
    string1 = "aabcc" #expect is "abcac", or "acabc"
    obj = Solution()
    result = obj.reorganizeString(string1)
    print("return result is "+result);

if __name__ =='__main__':
    main() 