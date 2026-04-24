# Binary Tree Inorder Traversal

## Problem Statement
Given the root of a binary tree, return the inorder traversal of its nodes' values. Inorder traversal visits the left subtree, the current node, and then the right subtree. For example, given the binary tree `[4,2,5,1,3]` where the nodes have the following structure:
        4
       / \
      2   5
     / \
    1   3
The inorder traversal is `[1,2,3,4,5]`. The binary tree node is defined as `struct TreeNode { int val; TreeNode *left; TreeNode *right; TreeNode() : val(0), left(nullptr), right(nullptr) {}; TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}; TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}; };`. 

## Approach
The algorithm uses a recursive or iterative approach to traverse the binary tree in inorder. It visits the left subtree, the current node, and then the right subtree. This can be achieved using a stack to store nodes or by using recursive function calls.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <vector>
using namespace std;
// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> result;
        // Using recursive approach to solve the problem
        // We can also use iterative approach with a stack
        
        // Recursive function to perform inorder traversal
        function<void(TreeNode*)> traverse = [&](TreeNode* node) {
            if (!node) return;
            traverse(node->left);  // visit left subtree
            result.push_back(node->val);  // visit current node
            traverse(node->right);  // visit right subtree
        };
        
        traverse(root);
        return result;
    }
};
```

## Test Cases
```
Input: root = [4,2,5,1,3]
Output: [1,2,3,4,5]
Input: root = [1]
Output: [1]
Input: root = []
Output: []
```

## Key Takeaways
- Inorder traversal visits the left subtree, the current node, and then the right subtree.
- We can use recursive or iterative approach with a stack to solve the problem.
- The time complexity of the solution is O(n), where n is the number of nodes in the binary tree.