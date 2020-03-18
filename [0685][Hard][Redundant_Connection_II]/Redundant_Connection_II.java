// leetcode time     cost : 1 ms
// leetcode memory   cost : 39.9 MB
// https://leetcode.com/problems/redundant-connection-ii/discuss/278105/topic
class Solution {
    int[] anc;// 并查集
    int[] parent;// record the father of every node to find the one with 2
                 // fathers,记录每个点的父亲，为了找到双入度点

    public int[] findRedundantDirectedConnection(int[][] edges) {
        anc = new int[edges.length + 1];
        parent = new int[edges.length + 1];
        int[] edge1 = null;
        int[] edge2 = null;
        int[] lastEdgeCauseCircle = null;
        for (int[] pair : edges) {
            int u = pair[0];
            int v = pair[1];

            if (anc[u] == 0)
                anc[u] = u;
            if (anc[v] == 0)
                anc[v] = v;// init the union-find set 初始化并查集

            if (parent[v] != 0) {// node v already has a father, so we just skip the union of this edge and check
                                 // if there will be a circle ，跳过 edge2,并记下 edge1,edge2
                edge1 = new int[] { parent[v], v };
                edge2 = pair;
            } else {
                parent[v] = u;
                int ancU = find(u);
                int ancV = find(v);
                if (ancU != ancV) {
                    anc[ancV] = ancU;
                } else { // meet a circle , 碰到了环
                    lastEdgeCauseCircle = pair;
                }
            }
        }
        // 如果是情况2、3，则根据有没有碰到环返回 edge1 或 edge2
        if (edge1 != null && edge2 != null)
            // 第2次遇到的2个入度的边没有加入 parent[]，anc[]时，
            // 如果形成 环 或 树（有公共祖先），则说明第一次遇到的2入度边在环内，删除该边，
            // 否则第2次遇到的边在环内，删除edge2
            return lastEdgeCauseCircle == null ? edge2 : edge1;
        else
            return lastEdgeCauseCircle; // 否则就是情况1，返回那个导致环的最后出现的边。
    }

    private int find(int node) {
        if (anc[node] == node)
            return node;
        anc[node] = find(anc[node]);
        return anc[node];
    }
}