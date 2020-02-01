/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
// leetcode time     cost : 1 ms
// leetcode memory   cost : 38.7 MB
class Solution {
    long pre = Long.MIN_VALUE;
    boolean flag = true;
    public boolean isValidBST(TreeNode root) {
        inOrder(root);
        return flag;
    }
    public void inOrder(TreeNode root)
    {
        if(root == null)
            return;
        inOrder(root.left);
        if(pre >= root.val){
            flag = false;
            return;
        }
        pre = root.val;
        inOrder(root.right);
    }    
}