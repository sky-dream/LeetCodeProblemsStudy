# leetcode time     cost : ---- ms
# leetcode memory   cost : ---- MB 
# Time  Complexity: O(N)
# Space Complexity: O(N)
from typing import List
class Solution:
    def alienOrder(self, words: List[str]) -> str:
      dic = self.build_dict(words)
      graph = self.build_adj(words, dic)
      path = []
      visited = [0 for _ in range(len(dic))]
      for i in range(len(dic)):
        if not visited[i]:
          state = self.dfs(i, graph, path, visited)
          if not state: return ""
      path.reverse()
      temp = {dic[k]:k for k in dic}
      ans = "".join([temp[i] for i in path])
      return ans

    def dfs(self, start, adj, path, visited):
      visited[start] = 1
      for next_node in adj[start]:
        if visited[next_node] == 1: return False
        if visited[next_node] == 2: continue
        state = self.dfs(next_node, adj, path, visited)
        if not state: return False
      visited[start] = 2
      path.append(start)
      return True
    
    def build_dict(self, words):
      dic = {}
      index = 0
      for word in words:
        for char in word:
          if char not in dic:
            dic[char] = index
            index += 1
      return dic

    def build_adj(self, words, dic):
      graph = {}
      for i in range(len(dic)):
        graph[i] = []
      for index, word in enumerate(words):
        if index < len(words) -1:
          i = 0
          while i< len(words[index]) and i < len(words[index+1]) and words[index][i] == words[index+1][i]:
            i += 1
          if i< len(words[index]) and i < len(words[index+1]):
            graph[dic[words[index][i]]].append(dic[words[index+1][i]])
      return graph

def main():
    words1 = ["ab","abc"]     # expect is "abc"
    obj = Solution()
    result = obj.alienOrder(words1)
    print("last return result is "+str(result));
    
    words2 = ["abc","ab"]     # expect is ""
    obj = Solution()
    result = obj.alienOrder(words2)
    print("last return result is "+str(result));
if __name__ =='__main__':
    main() 