# leetcode time     cost : 212 ms
# leetcode memory   cost : 13.9 MB 
# Time  Complexity: O(N+E)
# Space Complexity: O(N), the stack used to save color
# bipartite graph
class Solution(object):
    def isBipartite(self, graph):
        color = {}
        for node in range(len(graph)):
            if node not in color:
                stack = [node]
                color[node] = 0
                while stack:
                    node = stack.pop()
                    for nei in graph[node]:
                        if nei not in color:
                            stack.append(nei)
                            color[nei] = color[node] ^ 1
                        elif color[nei] == color[node]:
                            return False
        return True