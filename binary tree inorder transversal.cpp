#include <stack>
#include <vector>
#include <iostream>

struct TreeNode
{
	int val;
	TreeNode *left;
	TreeNode *right;
	TreeNode(int x) : val(x), left(NULL), right(NULL) {}  
};

class Solution
{
public:
	std::vector<int> inorderTraversal(TreeNode* root)
	{
		std::vector<int> result;
		std::stack<TreeNode*> stack;
		TreeNode* current = root;

		while (current != NULL || !stack.empty())    
		{
		
			while (current != NULL)
			{
				stack.push(current);
				current = current->left;
			}
			
			current = stack.top();
			stack.pop();
			result.push_back(current->val);
			
			current = current->right;
		}

		return result;
	}
};

int main()
{
	TreeNode* root = new TreeNode(1);
	root->right = new TreeNode(2);
	root->right->left = new TreeNode(3);

	Solution sol;
	std::vector<int> result = sol.inorderTraversal(root);


	std::cout << "Inorder Traversal: ";
for (int val : result)
	{
		std::cout << val << " ";
	}
	std::cout << std::endl;
	delete root->right->left;
	delete root->right;
	delete root;

	return 0;
}
