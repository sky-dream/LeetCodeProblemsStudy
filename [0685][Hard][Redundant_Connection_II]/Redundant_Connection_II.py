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
        # 发现了环，并且是一个有冲突的环，得考虑删哪个边，先删除最后一条边试试
        father, firsta = list(range(n+1)), -1
        for a, b in edges:
            if b != dupb:
                fa, fb = find(a), find(b)
                if fa != fb:
                    union(a, b)
                else:
                    return [firsta, dupb]
            elif a != dupa:
                # 指向冲突节点的第一条边
                firsta = a
                fa, fb = find(a), find(b)
                if fa != fb:
                    union(a, b)
                else:
                    return [firsta, dupb]
        # 删除 [dupa, dupb] 就没环了，这样就是结果
        return [dupa, dupb]


def main():
    graph1 = [[1,2], [1,3], [2,3]]      #expect is [2,3],example 1,   
    graph2 = [[1,2], [2,3], [3,4], [4,1], [1,5]]      #expect is [4,1],example 2,      
    obj = Solution()
    res = obj.findRedundantDirectedConnection(graph1)
    print("return value is ",res);
    
if __name__ =='__main__':
    main() 