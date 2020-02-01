#include <stdlib.h>
using namespace std;
/*   Definition for a binary tree node. */
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}

};
// leetcode time     cost : 28 ms
// leetcode memory   cost : 20.7 MB
//C++ inorder recursion:
class Solution {
public:
    TreeNode* pre;
    bool isValidBST(TreeNode* root) {        
        //solution with recursion.
        if(root == NULL)
            return true;
        if(!isValidBST(root->left)){
            return false;
        }
        if(pre && pre->val >= root->val)
            return false;
        pre = root;
        if(!isValidBST(root->right))
            return false;
        return true;            
    }
};