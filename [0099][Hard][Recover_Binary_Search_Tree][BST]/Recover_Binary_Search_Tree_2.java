//Definition for a binary tree node.
public class TreeNode {
    int val;
    TreeNode() {}
    TreeNode(int val) { this.val = val; }
    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
    TreeNode right;
    TreeNode left;
}

// Time  Complexity: O(N)
// Space Complexity: O(1)
// Solution 3, Morris inorder traversal
class Solution {
    public void recoverTree(TreeNode root) {
        TreeNode first = null, last = null;
        TreeNode pre = null, cur = root, tail = null;
        while (cur != null) {
            // 模板代码，和遍历相同
            tail = cur.left;
            if (tail != null) {
                // 找到 tail 位置
                while (tail.right != null && tail.right != cur) {
                    tail = tail.right;
                }
                if (tail.right == null) {
                    // 暂时链接，充当栈的作用
                    tail.right = cur;
                    cur = cur.left;
                    continue;
                } else {
                    // 断开链接，保证二叉树结构不变
                    tail.right = null;
                }
            }
            // 更新 first & last 节点
            if (pre != null && pre.val > cur.val) {
                last = cur;
                if (first == null) {
                    first = pre;
                }
            }
            // 更新 pre & cur 节点
            pre = cur;
            cur = cur.right;
        }
        // 交换
        first.val ^= last.val;
        last.val ^= first.val;
        first.val ^= last.val;
    }
}