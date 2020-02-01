/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
// leetcode time     cost : 0 ms
// leetcode memory   cost : 38.8 MB
public class Solution {

    long max = Long.MIN_VALUE;
    /**
     * 中序遍历时，判断当前root值是否增大了
     */
    public boolean isValidBST(TreeNode root) {
        if (root == null) {
            return true;
        }
        // 先判断左子树 再判断root 其次是右子树
        return isValidBST(root.left)  && visit(root) && isValidBST(root.right);
    }

    public boolean visit(TreeNode root) {
        if(root.val > max){
            // 增大记录最大值
            max = root.val;
            return true;
        }else{
            // 不满足
            return false;
        }
    }
}