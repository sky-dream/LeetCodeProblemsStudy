#include <stack>
using namespace std;
/*   Definition for a binary tree node. */
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}

};
// leetcode time     cost : 12 ms
// leetcode memory   cost : 20.8 MB
class Solution {
public:
    TreeNode* pre;
    bool isValidBST(TreeNode* root) {
        //cpp solution 1, use stack from cpp std lib without recursion.
        stack<TreeNode*> s;
        TreeNode* cur = root;  
        while(!s.empty() || cur){
            if(cur){
                s.push(cur);
                cur = cur->left;
            }else{
                cur = s.top();
                s.pop();
                if(pre && pre->val >= cur->val) return false;
                pre = cur;
                cur = cur->right;
            }
        }
        return true;            
    }
};
int main(){
    return 0;
}