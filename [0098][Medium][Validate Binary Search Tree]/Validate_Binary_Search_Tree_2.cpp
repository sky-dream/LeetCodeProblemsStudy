#include <stdlib.h>
using namespace std;
/*   Definition for a binary tree node. */
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}

};
// leetcode time     cost : 32 ms
// leetcode memory   cost : 20.8 MB
//C++ inorder recursion:
class Solution {
public:
    int* last = NULL;
    bool isValidBST(TreeNode* root) {
        if (root){
            if(!isValidBST(root->left)) 
                return false;
            if (last && *last>=root->val) 
                return false;
            last = &root->val;
            if(!isValidBST(root->right)) 
                return false;
            return true;
        }
        else 
            return true;
    };
};