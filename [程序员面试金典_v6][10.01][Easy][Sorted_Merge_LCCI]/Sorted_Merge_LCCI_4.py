# loop array A[] with a reverse order.
class Solution:
    def merge(self, A: List[int], m: int, B: List[int], n: int) -> None:
        """
        Do not return anything, modify A in-place instead.
        """
        idx_a = m-1
        idx_b = n-1
        if len(A) < m+n:
            A = A + [0 for i in range(len(A)-m)]
        # handle if B is null or empty or n=0
        if not n:
            A[:] = A[:m]
            return 

        # handle if A is null or empty or m=0
        if not m:
            A[:] = B[:n]
            return      
        # handle if A,B,m,n all not 0 or empty
        for i in range(m+n-1,-1,-1):
            if (A[idx_a]>=B[idx_b]) and idx_a>=0:
                A[i] = A[idx_a]
                idx_a -= 1  
            elif idx_b>=0:
                A[i] = B[idx_b]
                idx_b -= 1
        return 