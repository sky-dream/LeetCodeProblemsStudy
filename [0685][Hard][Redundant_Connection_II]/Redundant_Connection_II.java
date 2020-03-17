// leetcode time     cost : 1 ms
// leetcode memory   cost : 39.9 MB
// https://leetcode.com/problems/redundant-connection-ii/discuss/278105/topic
class Solution {  
    int[] ancester;//并查集
    int[] parent;// record the father of every node to find the one with 2 fathers,记录每个点的父亲，为了找到双入度点
    public int[] findRedundantDirectedConnection(int[][] edges) {
        ancester=new int[edges.length+1];
        parent=new int[edges.length+1];
        int[] edge1=null;
        int[] edge2=null;
        int[] lastEdgeCauseCircle=null;
        for (int[] pair:edges){
            int u=pair[0];
            int v=pair[1];
            
            if(ancester[u]==0) ancester[u]=u;
            if(ancester[v]==0) ancester[v]=v;//init the union-find set  初始化并查集
                
            if (parent[v]!=0){// node v already has a father, so we just skip the union of this edge and check if there will be a circle ，跳过 edge2,并记下 edge1,edge2
                edge1=new int[]{parent[v],v};
                edge2=pair;
            } else {
                parent[v]=u;
                int ancesterU=find(u);
                int ancesterV=find(v);
                if(ancesterU!=ancesterV){
                    ancester[ancesterV]=ancesterU;
                } else { //meet a circle , 碰到了环
                    lastEdgeCauseCircle=pair;
                }
            }
        }
        if (edge1!=null&&edge2!=null) return lastEdgeCauseCircle==null?edge2:edge1; //如果是情况2、3，则根据有没有碰到环返回 edge1 或 edge2
        else return lastEdgeCauseCircle; //否则就是情况1，返回那个导致环的最后出现的边。
    }
     
    private int find(int node){
        if (ancester[node]==node) return node;
        ancester[node]=find(ancester[node]);
        return ancester[node];
    }
}