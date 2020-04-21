// leetcode time     cost : ---- ms
// leetcode memory   cost : ---- MB
import java.util.Arrays;
import java.util.Stack;
import java.util.HashSet;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.ArrayList;
import java.lang.Character;
class Solution {
// 基本情况处理，比如输入为空，或者输入的字符串只有一个
String alienOrder(String[] words) {
    if (words == null || words.length == 0)
        return null;
    if (words.length == 1) {
        return words[0];
    }
  
    // 构建有向图：定义一个邻接链表 adjList，也可以用邻接矩阵
    Map<Character, List<Character>> adjList = new HashMap<>();

    for (int i = 0; i < words.length - 1; i++) {
        String w1 = words[i], w2 = words[i + 1];
        int n1 = w1.length(), n2 = w2.length();

        boolean found = false;
    
        for (int j = 0; j < Math.max(w1.length(), w2.length()); j++) {
            Character c1 = j < n1 ? w1.charAt(j) : null;
            Character c2 = j < n2 ? w2.charAt(j) : null;

            if (c1 != null && !adjList.containsKey(c1)) {
                adjList.put(c1, new ArrayList<Character>());
            }

            if (c2 != null && !adjList.containsKey(c2)) {
                adjList.put(c2, new ArrayList<Character>());
            }

            if (c1 != null && c2 != null && c1 != c2 && !found) {
                adjList.get(c1).add(c2);
                found = true;
            }
        }
    }

    Set<Character> visited = new HashSet<>();
    Set<Character> loop = new HashSet<>();
    Stack<Character> stack = new Stack<Character>();
  
    for (Character key : adjList.keySet()) {
        if (!visited.contains(key)) {
            if (!topologicalSort(adjList, key, visited, loop, stack)) {
                return "";
            }
        }
    }

    StringBuilder sb = new StringBuilder();

    while (!stack.isEmpty()) {
        sb.append(stack.pop());
    }

    return sb.toString();
  
} 
        // 将当前节点 u 加入到 visited 集合以及 loop 集合中。
        boolean topologicalSort(Map<Character, List<Character>> adjList, char u, 
                                Set<Character> visited, Set<Character> loop, Stack<Character> stack) {
            visited.add(u);
            loop.add(u);

            if (adjList.containsKey(u)) {
                for (int i = 0; i < adjList.get(u).size(); i++) {
                    char v = adjList.get(u).get(i);
        
                    if (loop.contains(v))
                        return false;
                
                    if (!visited.contains(v)) {
                        if (!topologicalSort(adjList, v, visited, loop, stack)) {
                            return false;
                        }
                    }
                }
            }
            loop.remove(u);
            stack.push(u);
            return true;
        }     
}

public class Alien_Dictionary {
    public static void main(String args[]) {
        String[] words= {"ab","abc"}; // #expect is "abc"
        Solution Solution_obj = new Solution();
        String result = Solution_obj.alienOrder(words);
        System.out.println("In java code,return value is :" + result);
    }
}