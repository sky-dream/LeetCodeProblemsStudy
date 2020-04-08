# leetcode time     cost : 40 ms
# leetcode memory   cost : 13.7 MB
# Time  Complexity: O(N**N)
# Space  Complexity: O(N)
# solution 1. dfs with memory

import collections


class Solution(object):
    def numSquarefulPerms(self, A):
        N = len(A)
        count = collections.Counter(A)

        graph = {x: [] for x in count}
        for x in count:
            for y in count:
                if int((x+y)**.5 + 0.5) ** 2 == x+y:
                    graph[x].append(y)

        def dfs(x, todo):
            count[x] -= 1
            if todo == 0:
                ans = 1
            else:
                ans = 0
                for y in graph[x]:
                    if count[y]:
                        ans += dfs(y, todo - 1)
            count[x] += 1
            return ans

        return sum(dfs(x, len(A) - 1) for x in count)


def main():
    A = [1, 17, 8]  # expect is 2
    obj = Solution()
    res = obj.numSquarefulPerms(A)
    print("return value is ", res)


if __name__ == '__main__':
    main()
