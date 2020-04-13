// leetcode time     cost : 2 ms
// leetcode memory   cost : 40 MB 
// Time  Complexity: O(n)
// Space Complexity: O(n)

/**
 * Definition for a binary tree node.
 */
public class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode(int x) {
        val = x;
    }
}

// # solution 1, 3 times loop for left boundary, leaves, right boundary,
public class Solution {

    public boolean isLeaf(TreeNode t) {
        return t.left == null && t.right == null;
    }

    public void addLeaves(List<Integer> res, TreeNode root) {
        if (isLeaf(root)) {
            res.add(root.val);
        } else {
            if (root.left != null) {
                addLeaves(res, root.left);
            }
            if (root.right != null) {
                addLeaves(res, root.right);
            }
        }
    }

    public List<Integer> boundaryOfBinaryTree(TreeNode root) {
        ArrayList<Integer> res = new ArrayList<>();
        if (root == null) {
            return res;
        }
        if (!isLeaf(root)) {
            res.add(root.val);
        }
        TreeNode tmp = root.left;
        while (tmp != null) {
            if (!isLeaf(tmp)) {
                res.add(tmp.val);
            }
            if (tmp.left != null) {
                tmp = tmp.left;
            } else {
                tmp = tmp.right;
            }

        }
        addLeaves(res, root);
        Stack<Integer> s = new Stack<>();
        tmp = root.right;
        while (tmp != null) {
            if (!isLeaf(tmp)) {
                s.push(tmp.val);
            }
            if (tmp.right != null) {
                tmp = tmp.right;
            } else {
                tmp = tmp.left;
            }
        }
        while (!s.empty()) {
            res.add(s.pop());
        }
        return res;
    }
}