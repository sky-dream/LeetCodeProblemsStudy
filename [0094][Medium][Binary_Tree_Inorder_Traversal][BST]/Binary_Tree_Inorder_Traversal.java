//Definition for a binary tree node.
public class TreeNode {
     int val;
    TreeNode left;
     TreeNode right;
     TreeNode(int x) { val = x; }
}

// Time  Complexity: O(N)
// Space Complexity: O(N)
// Solution 1, recursion
class Solution {
    public List < Integer > inorderTraversal(TreeNode root) {
        List < Integer > res = new ArrayList < > ();
        helper(root, res);
        return res;
    }

    public void helper(TreeNode root, List < Integer > res) {
        if (root != null) {
            if (root.left != null) {
                helper(root.left, res);
            }
            res.add(root.val);
            if (root.right != null) {
                helper(root.right, res);
            }
        }
    }
}