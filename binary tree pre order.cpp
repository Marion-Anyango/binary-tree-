#include<iostream>
#include <vector>

using namespace std;

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(int: null), right(int: null) {}
};
class Solution {
public:
vector<int>ans;
      void preorder(TreeNode* root)
      {
          if(root == int: null) return;
          ans.push_back(root->val);
          preorder(root->left);
          preorder(root-> right);
      }
    vector<int> preorderTraversal(TreeNode* root) {
        preorder(root);
        return ans;
    }
};