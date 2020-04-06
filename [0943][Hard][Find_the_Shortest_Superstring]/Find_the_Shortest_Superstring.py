# leetcode time     cost : 824 ms
# leetcode memory   cost : 14.8 MB 
# Time  Complexity: O(n^2 * 2^n)
# Space Complexity: O(n * 2^n)
# solution 2, DP
class Solution(object):
    def shortestSuperstring(self, A):
        N = len(A)

        # Populate overlaps
        overlaps = [[0] * N for _ in range(N)]
        for i, x in enumerate(A):
            for j, y in enumerate(A):
                if i != j:
                    for ans in range(min(len(x), len(y)), -1, -1):
                        if x.endswith(y[:ans]):
                            overlaps[i][j] = ans
                            break

        # dp[mask][i] = most overlap with mask, ending with ith element
        dp = [[0] * N for _ in range(1<<N)]
        parent = [[None] * N for _ in range(1<<N)]
        for mask in range(1, 1 << N):
            for bit in range(N):
                if (mask >> bit) & 1:
                    # Let's try to find dp[mask][bit].  Previously, we had
                    # a collection of items represented by pmask.
                    pmask = mask ^ (1 << bit)
                    if pmask == 0: continue
                    for i in range(N):
                        if (pmask >> i) & 1:
                            # For each bit i in pmask, calculate the value
                            # if we ended with word i, then added word 'bit'.
                            value = dp[pmask][i] + overlaps[i][bit]
                            if value > dp[mask][bit]:
                                dp[mask][bit] = value
                                parent[mask][bit] = i

        # Answer will have length sum(len(A[i]) for i) - max(dp[-1])
        # Reconstruct answer:

        # Follow parents down backwards path that retains maximum overlap
        perm = []
        mask = (1<<N) - 1
        i = max(range(N), key = dp[-1].__getitem__)
        while i is not None:
            perm.append(i)
            mask, i = mask ^ (1<<i), parent[mask][i]

        # Reverse path to get forwards direction; add all remaining words
        perm = perm[::-1]
        seen = [False] * N
        for x in perm:
            seen[x] = True
        perm.extend([i for i in range(N) if not seen[i]])

        # Reconstruct answer given perm = word indices in left to right order
        ans = [A[perm[0]]]
        for i in range(1, len(perm)):
            overlap = overlaps[perm[i-1]][perm[i]]
            ans.append(A[perm[i]][overlap:])

        return "".join(ans)

def main():
    A = ["alex","loves","leetcode"]      #expect is alexlovesleetcode
    obj = Solution()
    res = obj.shortestSuperstring(A)
    print("return value is ",res);
    
if __name__ =='__main__':
    main()   