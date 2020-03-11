# leetcode time     cost : 124 ms
# leetcode memory   cost : 16.6 MB
# Time  Complexity: O(1)
# Space Complexity: O(MN)
# solution1, DP
# https://leetcode-cn.com/problems/range-sum-query-2d-immutable/solution/er-wei-qu-yu-he-jian-suo-ju-zhen-bu-ke-bian-by-lee/


class NumMatrix:

    def __init__(self, matrix):
        if not matrix:
            return
        maxRow = len(matrix)
        maxCol = len(matrix[0])
        # sumPoint[i][j] is the sum of rectangle use [0][0] as left top,use [i][j] as right bottom
        self.sumPoint = [[0]*(maxCol+1) for _ in range(maxRow+1)]
        for i in range(maxRow):
            for j in range(maxCol):
                self.sumPoint[i+1][j+1] = self.sumPoint[i+1][j] + \
                    self.sumPoint[i][j+1] + matrix[i][j] - self.sumPoint[i][j]

    # def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

    def sumRegion(self, row1, col1, row2, col2):
        return self.sumPoint[row2 + 1][col2 + 1] - self.sumPoint[row1][col2 + 1] - self.sumPoint[row2 + 1][col1] + self.sumPoint[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

def main():
    matrix = [[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [
        1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]
    operation = ["NumMatrix", "sumRegion", "sumRegion", "sumRegion"]
    indexGroup = [[matrix], [2, 1, 4, 3], [1, 1, 2, 2], [1, 2, 2, 4]]
    # expect is [null,8,11,12]
    obj = NumMatrix(matrix)
    print(None)
    for i in range(1, len(operation)):
        #print("operation: ",operation[i],",parameter: ",indexGroup[i][0])
        cmd = 'obj.'+operation[i]+"(%r,%r,%r,%r)" % (indexGroup[i]
                                                     [0], indexGroup[i][1], indexGroup[i][2], indexGroup[i][3])
        result = eval(cmd)
        print("result: ", result)


if __name__ == '__main__':
    main()
