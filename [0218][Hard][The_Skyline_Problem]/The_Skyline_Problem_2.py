# leetcode time     cost : 544 ms
# leetcode memory   cost : 18.4 MB 
# Time  Complexity: O(N*logN)
# Space Complexity: O(N)
# solution 2, Bisection method,二分法, line scan
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        import bisect
        res = [[0, 0]]
        # 记录 [left, height], [right, height]
        loc = []
        for l, r, h in buildings:
            # 为了排序让 left那边靠前, 所以让高度取负
            loc.append([l, -h])
            loc.append([r, h])
        loc.sort()
        heap = [0]

        for x, h in loc:
            if h < 0:
                bisect.insort(heap, h)
            else:
                heap.remove(-h)
            cur = -heap[0]
            if res[-1][1] != cur:
                res.append([x, cur])

        return res[1:]