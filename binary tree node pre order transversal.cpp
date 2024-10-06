#include <iostream>
#include <vector>

using namespace std;

// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {} // Constructor
};

class Solution {
public:
    // Function to perform preorder traversal
    vector<int> preorderTraversal(TreeNode* root) {
        vector<int> result;  // Vector to store the traversal result
        preorder(root, result);
        return result;
    }

private:
    // Helper function for preorder traversal
    void preorder(TreeNode* node, vector<int>& result) {
        if (node == nullptr) return;  // Base case: if the node is null, return
        result.push_back(node

