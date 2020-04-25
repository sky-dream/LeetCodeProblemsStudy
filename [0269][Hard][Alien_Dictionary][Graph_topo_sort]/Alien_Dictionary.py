# leetcode time     cost : 52 ms
# leetcode memory   cost : 13.8 MB 
# Time  Complexity: O(N)
# Space Complexity: O(N)
from typing import List
class Solution:
    def __init__(self):
      self.solutionNotFound = False
      
    def alienOrder(self, words: List[str]) -> str:
      # init the char mapping table
      dic = self.build_dict(words)
      print("char mapping dict: ",dic)
      # create adjacent list
      graph = self.build_adj(words, dic)
      print("adjacent list: ",graph)
      path = []
      # finish topo sort
      visited = [-1 for _ in range(len(dic))]
      for k,v in dic.items():
        if visited[v] is -1:
          state = self.dfs(v, graph, path, visited)
          if not state: return ""
      path.reverse()
      
      dictIndexToChar = {dic[k]:k for k in dic}
      ans = "".join([dictIndexToChar[i] for i in path])
      return ans if not self.solutionNotFound else ""

    def dfs(self, start, adj, path, visited):
      visited[start] = 1
      for next_node in adj[start]:
        # =1 means circle found
        if visited[next_node] == 1: 
          return False
        # =2 means this node checked before
        if visited[next_node] == 2: continue
        state = self.dfs(next_node, adj, path, visited)
        if not state: 
          return False
      visited[start] = 2
      path.append(start)
      #print(path,",current start is: ",start)
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
      
      for index in range( len(words)-1 ):
        w1,w2 = words[index],words[index+1]
        n1,n2 = len(w1),len(w2) 
        charOrderFound = False
        for j in range( max(n1,n2) ):
          c1 = w1[j] if j < n1 else None
          c2 = w2[j] if j < n2 else None
          if (c1) and (c2) and (c1 != c2) and (not charOrderFound):
            charOrderFound = True
            if dic[c2] not in graph[dic[c1]]:
              graph[dic[c1]].append(dic[c2])
          # used to handle case ["abc","ab"]
          if((c1 == c2) and ((j+1) == n2) and (n1>n2) and (not charOrderFound)):
            self.solutionNotFound = True
      return graph

def main():  
    words1,expect1 = ["wrt","wrf","er","ett","rftt"],"wertf"
    words2,expect2 = ["abc","ab"],""
    words3,expect3 = ["ab","abc"],"abc"
    words4,expect4 = ["ab","adc"],"abcd"
    words5,expect5 = ["za","zb","ca","cb"],"abzc"
    testCases = [(words1,expect1),(words2,expect2),(words3,expect3),(words4,expect4),(words5,expect5)]
    for input_strs,expectRes in testCases:
        obj = Solution()
        print("******************new test start,input is: ",input_strs,"********************")
        result = obj.alienOrder(input_strs)
        try:
            assert result == expectRes
            print("passed, result is follow expect:",result)
        except AssertionError as aError:
            print('failed, result >> ', result,"<< is wrong, ","expect is : "+ expectRes)
if __name__ =='__main__':
    main() 