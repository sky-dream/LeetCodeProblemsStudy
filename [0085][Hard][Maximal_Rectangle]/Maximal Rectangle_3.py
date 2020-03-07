# -*- coding: utf-8 -*-  
# leetcode time     cost : 152 ms
# leetcode memory   cost : 14.3 MB
# solution 4, DP,check the max height, left extended width, right extended width,
class Solution:

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix: return 0

        m = len(matrix)
        n = len(matrix[0])

        left = [0] * n # initialize left as the leftmost boundary possible
        right = [n] * n # initialize right as the rightmost boundary possible
        height = [0] * n

        maxarea = 0

        for i in range(m):

            cur_left, cur_right = 0, n
            # update height
            for j in range(n):
                if matrix[i][j] == '1': 
                    height[j] += 1
                else: 
                    height[j] = 0
            # update left boundary index from left to right, cur_left represents the left_index_border +1 to make calculation simple 
            for j in range(n):
                if matrix[i][j] == '1': 
                    left[j] = max(left[j], cur_left)
                else:
                    left[j] = 0
                    cur_left = j + 1
            # update right boundary index from right to left,cur_right represents the right_index_border +1 to make calculation simple 
            for j in range(n-1, -1, -1):
                if matrix[i][j] == '1': 
                    right[j] = min(right[j], cur_right)
                else:
                    right[j] = n
                    cur_right = j
            # update the area
            for j in range(n):
                maxarea = max(maxarea, height[j] * (right[j] - left[j]))

        return maxarea


def main():
    matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]  # expect is 6
    Solution_obj = Solution()
    result = Solution_obj.maximalRectangle(matrix)
    print("result value is ",result)
    
if __name__ =='__main__':
    main()  