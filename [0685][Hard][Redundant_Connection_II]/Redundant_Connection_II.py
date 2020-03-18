# -*- coding: utf-8 -*-
# leetcode time     cost : 88 ms
# leetcode memory   cost : 14.1 MB


class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        father = list(range(n+1))
        indegree = [0] * (n+1)

        def find(x):
            f = x
            while f != father[f]:
                f = father[f]
            while f != x:
                x, father[x] = father[x], f
            return f

        def union(x, y):
            father[find(y)] = find(x)
        lasta, lastb, dupa, dupb = -1, -1, -1, -1
        for a, b in edges:
            indegree[b] += 1
            if indegree[b] == 2:
                dupa, dupb = a, b
            fa, fb = find(a), find(b)
            if fa != fb:
                union(a, b)
            else:
                lasta, lastb = a, b
        if dupb == -1:
            # 如果发现了环，还没发现入度为2的点，说明是一个顺序环，随便删
            return [lasta, lastb]
        # 发现了环，并且是一个有冲突的环 (环内存在不同方向的边)，得考虑删哪个边，先删除最后一条边试试
        father, firsta = list(range(n+1)), -1
        for a, b in edges:
            # 遍历除 2个入度为2的边 以外的所有边，
            if b != dupb:
                fa, fb = find(a), find(b)
                if fa != fb:
                    union(a, b)
                # 此时如果可以发现新加入的一条边对应的2个node有公共祖先，则说明此时存在 环 或 存在一个合法的树，
                # 则说明第一次遇到的2个入度的边[firsta, dupb]在环内，可以删除这条边，
                # 否则若没遇到公共祖先，则说明第2次遇到的边[dupa, dupb]在环内，可以删除这条边[dupa, dupb]
                else:
                    return [firsta, dupb]
            # 向father中加入第一次出现的2个入度的边，检测是否存在 树 或 环
            elif a != dupa:
                # 指向冲突节点的第一条边
                firsta = a
                fa, fb = find(a), find(b)
                if fa != fb:
                    union(a, b)
                # 此时如果可以发现新加入的一条边对应的2个node有公共祖先，则说明此时存在 环 或 存在一个合法的树，
                # 则说明第一次遇到的2个入度的边[firsta, dupb]在环内，可以删除这条边，
                # 否则若没遇到公共祖先，则说明第2次遇到的边[dupa, dupb]在环内，可以删除这条边[dupa, dupb]
                else:
                    return [firsta, dupb]
        # 删除 [dupa, dupb] 就没环了，这样就是结果
        return [dupa, dupb]


def main():
    graph1 = [[1, 2], [1, 3], [2, 3]]  # expect is [2,3],example 1,
    graph2 = [[1, 2], [2, 3], [3, 4], [4, 1],
              [1, 5]]  # expect is [4,1],example 2,
    obj = Solution()
    res = obj.findRedundantDirectedConnection(graph1)
    print("return value is ", res)


if __name__ == '__main__':
    main()
