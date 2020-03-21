# leetcode time     cost : 44 ms
# leetcode memory   cost : 13.3 MB 
# Time  Complexity: O(logN)
# Space Complexity: O(logN)
# solution 2, matrix expo
class Solution(object):
    def numTilings(self, N):
        MOD = 10**9 + 7

        def matrix_mult(A, B):
            # transpose the matrix, refer to No.867
            ZB = list(zip(*B))
            #print("matrix_mult, B ",B,",A ",A)
            return [[sum(a * b for a, b in zip(row, col)) % MOD
                     for col in ZB] for row in A]

        def matrix_expo(A, K):
            if K == 0:
                return [[+(i==j) for j in range(len(A))]
                        for i in range(len(A))]
            if K == 1:
                return A
            elif (K%2):
                subResult = matrix_expo(A, K-1)
                return matrix_mult(subResult, A)
            subResult = matrix_expo(A, K/2)
            return matrix_mult(subResult, subResult)

        T = [[1, 0, 0, 1],
             [1, 0, 1, 0],
             [1, 1, 0, 0],
             [1, 1, 1, 0]]
        return matrix_expo(T, N)[0][0]

def main():
    n = 4      #expect is 11
    obj = Solution()
    res = obj.numTilings(n)
    print("return value is ",res);
    
if __name__ =='__main__':
    main()  
# Matrix multiply
def matrixMul(A, B):
    if len(A[0]) == len(B):
        res = [[0] * len(B[0]) for i in range(len(A))]
        for i in range(len(A)):
            for j in range(len(B[0])):
                for k in range(len(B)):
                    res[i][j] += A[i][k] * B[k][j]
        return res
    return ('输入矩阵有误！')