// leetcode time     cost : 3 ms
// leetcode memory   cost : 41.3 MB 
// Time  Complexity: O(N)
// Space Complexity: O(N)
// solution 1, DP
import java.util.HashMap;
import java.util.Map;
class Solution {
    Map<TreeNode, Integer> memo = new HashMap<>();
    public int rob(TreeNode root) {
        if (root == null) return 0;
        // 利用备忘录消除重叠子问题
        if (memo.containsKey(root)) 
            return memo.get(root);
        // 抢，然后去下下家
        int do_it = root.val
            + (root.left == null ? 
                0 : rob(root.left.left) + rob(root.left.right))
            + (root.right == null ? 
                0 : rob(root.right.left) + rob(root.right.right));
        // 不抢，然后去下家
        int not_do = rob(root.left) + rob(root.right);
        
        int res = Math.max(do_it, not_do);
        memo.put(root, res);
        return res;
    }
}

  //Definition for a binary tree node.
class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x) { val = x; }
}
