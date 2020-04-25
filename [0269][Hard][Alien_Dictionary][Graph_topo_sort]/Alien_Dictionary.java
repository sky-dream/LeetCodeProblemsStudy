// leetcode time     cost : 29 ms
// leetcode memory   cost : 40.3 MB
import java.lang.Character;
import java.util.ArrayDeque;
import java.util.HashMap;
import java.util.Map;
import java.util.ArrayList;
import java.util.List;
import java.util.Queue;
//import java.util.Stack;
class Solution {
    // 基本情况处理，比如输入为空，或者输入的字符串只有一个
    public String alienOrder(String[] words) {
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
                    //一个char1 可能多次指向 char2, 同一起点和终点只统计一次 
                    if(!adjList.get(c1).contains(c2)){
                        adjList.get(c1).add(c2);
                    }
                    // 字符不等, 说明出现了大于的关系, 记录下来,后面不用看了
                    found = true;
                }
                // used to handle case ["abc","ab"]
                if(c1 == c2 && (j+1) == n2 && n1>n2 && !found)
                    return ""; 
            }
        }
        System.out.println("adjList:  "+adjList.toString());

        StringBuilder strBuilder = new StringBuilder();
        // 拓补排序
        boolean sortResult = topologicalSort(adjList, strBuilder);
        if (sortResult){
            return strBuilder.toString();
        }
        else{
            return ""; 
        }
    
    } 
    // 拓补排序
    boolean topologicalSort(Map<Character, List<Character>> adjList,StringBuilder strBuilder) {
        Queue<Character> nodeHeader = new ArrayDeque<Character>();
        Map<Character, Integer> indegreeMap = new HashMap<>();
        //获取 indegree 入度表 
        for (Character key : adjList.keySet()) {
            if (!indegreeMap.containsKey(key)) {
                indegreeMap.put(key, 0);
            }
            
            for (Character c1 : adjList.get(key)) {
                if (!indegreeMap.containsKey(c1)) {
                    indegreeMap.put(c1, 1);
                }
                else{
                    int tmp = indegreeMap.get(c1);
                    indegreeMap.put(c1, tmp+1);
                }
            }
        }
        System.out.println("indegreeMap:  "+indegreeMap.toString());
        //把所有入度为0的字符节点加入到 Stack nodeHeader
        for (Character c1 : indegreeMap.keySet()){
            if (indegreeMap.get(c1)==0){
                nodeHeader.add(c1);
            }
        }
        //开始拓补排序
        while(!nodeHeader.isEmpty())
        {
            Character header=nodeHeader.poll(); // queue--poll(), stack---pop(),
            strBuilder.append(header);
            System.out.print("header: "+header+", ");
            
            for(Character c1 : adjList.get(header))
            {
                int tmp = indegreeMap.get(c1);
                if(tmp==1)//如果入度为1,那么header 是最后一个指向 c1的连接
                {
                    nodeHeader.add(c1);
                    indegreeMap.put(c1, 0);
                }
                else{
                    indegreeMap.put(c1, tmp-1);
                }
                //System.out.println(",dest is:  "+c1+", indegree value: "+tmp);
            }
        }
        // 如果拓扑排序遍历了所有的字符, 说明有可行解; 
        // 否则的话说明 1.不是有向无环图, 2.有环, 3.没有可行解
        if (adjList.keySet().size() == strBuilder.length()){
            return true;
        }
        else{
            return false;
        }
        
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