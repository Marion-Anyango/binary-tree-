#include <vector>
#include <stack>
#include <windows.h>

int WINAPI WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, LPSTR lpCmdLine, int nShowCmd)
{
	return 0;
}


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
	std::vector<int> postorderTraversal(TreeNode* root)
	{
		std::vector<int> result;
		if (!root) return result;

		std::stack<TreeNode*> stack;
		TreeNode* lastVisited = NULL;  
		stack.push(root);

		while (!stack.empty())
		{
			TreeNode* current = stack.top();

			if (!lastVisited || lastVisited->left == current || lastVisited->right == current)
			{
				if (current->left)
				{
					stack.push(current->left);
				}
				else if (current->right)
				{
					stack.push(current->right);
				}
				else
				{
					stack.pop();
					result.push_back(current->val);
					lastVisited = current;
				}
			}
			else if (current->right == lastVisited)
			{
				stack.pop();
				result.push_back(current->val);
				lastVisited = current;
			}
			else
			{
				if (current->right)
				{
					stack.push(current->right);
				}
			}
		}

		return result;
	}
};
