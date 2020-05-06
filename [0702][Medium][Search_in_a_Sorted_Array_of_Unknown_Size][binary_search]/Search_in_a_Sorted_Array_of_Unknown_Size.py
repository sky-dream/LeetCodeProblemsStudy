# leetcode time     cost : 44 ms
# leetcode memory   cost : 14.6 MB 
# Time  Complexity: O(logT)
# Space Complexity: O(1)
# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
class ArrayReader:
    def __init__(self,inputArray):
        self.array = inputArray
            
    def get(self, index: int) -> int:
        return self.array[index] if index<len(self.array) else None

# binary search
class Solution:
    def search(self, reader, target):
        if reader.get(0) == target:
            return 0
        
        # search boundaries
        left, right = 0, 1
        while reader.get(right) < target:
            left = right
            right <<= 1
        
        # binary search
        while left <= right:
            pivot = left + ((right - left) >> 1)
            num = reader.get(pivot)
            
            if num == target:
                return pivot
            if num > target:
                right = pivot - 1
            else:
                left = pivot + 1
        
        # there is no target element
        return -1
def main():
    reader, target,expectRes = [-1,0,3,5,9,12],9,4
    obj = Solution()
    result = obj.search(ArrayReader(reader), target)
    try:
        assert result == expectRes
        print("passed, result is follow expect:",result)
    except AssertionError as aError:
        print('failed, result >> ', result,"<< is wrong, ","expect is : "+ expectRes)
    
if __name__ =='__main__':
    main() 