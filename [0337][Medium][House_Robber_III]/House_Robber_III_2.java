// leetcode time     cost : 1 ms
// leetcode memory   cost : 41.4 MB 
// Time  Complexity: O(N)
// Space Complexity: O(1)
// solution 1, DP
class Solution {
    int rob(TreeNode root) {
        int[] res = dp(root);
        return Math.max(res[0], res[1]);
    }
    
    /* arr size is 2
    arr[0] do not rob root, the max money
    arr[1] do not rob root, the max money */
    int[] dp(TreeNode root) {
        if (root == null)
            return new int[]{0, 0};
        int[] left = dp(root.left);
        int[] right = dp(root.right);
        // rob the root, the next node can not rob
        int rob = root.val + left[0] + right[0];
        // not rob root, the next node can rob or not, based on the result
        int not_rob = Math.max(left[0], left[1])
                    + Math.max(right[0], right[1]);
        
        return new int[]{not_rob, rob};
    }
}

  //Definition for a binary tree node.
class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x) { val = x; }
}
