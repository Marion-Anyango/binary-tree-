#include <iostream>
#include <algorithm>
using namespace std;
struct treenode
{
	int val;
	treenode*left;
	treenode*right;
	treenode(int x): val(x), left(NULL), right(NULL)
	{

	}
};
class solution
{
public:
	int checkheight(treenode*node)
	{
		if (!node)return 0;
		int leftheight = checkheight(node->left);
		if (leftheight == -1)return -1;
		int rightheight = checkheight(node->right);
		if (rightheight == -1)return -1;
		if(abs(leftheight - rightheight) > 1)return -1;
		return max(leftheight, rightheight) + 1;
	}
		bool isbalanced(treenode * root)
		{
			return checkheight(root) != -1;
		}

	};
	int main()
	{
		treenode*root = new treenode(1);
		root->left = new treenode(2);
		root->right = new treenode(3);
		root->left->left = new treenode(4);
		root->left->right = new treenode(5);
		solution sol;
		if(sol.isbalanced(root))
			cout << "the tree is balanced" << endl;
		else
			cout << "the tree is not balanced" << endl;
		return 0;
	}

