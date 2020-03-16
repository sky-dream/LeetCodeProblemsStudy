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
                    for neighbor in graph[node]:
                        if neighbor not in color:
                            stack.append(neighbor)
                            color[neighbor] = color[node] ^ 1
                        elif color[neighbor] == color[node]:
                            return False
        return True

def main():
    graph1 = [[1,3],[0,2],[1,3],[0,2]]      #expect is true,example 1,   
    graph2 = [[1,2,3], [0,2], [0,1,3], [0,2]]      #expect is false,example 2,      
    obj = Solution()
    res = obj.isBipartite(graph1)
    print("return value is ",res);
    
if __name__ =='__main__':
    main()   