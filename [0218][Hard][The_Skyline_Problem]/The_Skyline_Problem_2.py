# leetcode time     cost : 544 ms
# leetcode memory   cost : 18.4 MB 
# Time  Complexity: O(N*logN)
# Space Complexity: O(N)
# solution 2, Bisection method,二分法, line scan
class Solution:
    def getSkyline(self, buildings: [[int]]):
        import bisect
        res = []
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
                # keep the heightest at the first index
                bisect.insort(heap, h)
                # 1. bisect.insort(listX, x)       
                # 2. listX.append(x), listX.sort(),
                # 3. heapq.heappush(listX, x)
            # if reached right index(h>0), then pop out this building's height from heap, stop use it.
            else:
                heap.remove(-h)
            # get the biggest height by the building left index from left to right 
            cur = -heap[0]
            # if the height is not as before line point, add this new point
            if len(res)==0 or res[-1][1] != cur:
                res.append([x, cur])

        return res