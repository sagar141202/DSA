# Binary Tree Inorder Traversal

## Problem Statement
Given the root of a binary tree, return the inorder traversal of its nodes' values. Inorder traversal visits the left subtree, the current node, and then the right subtree. For example, given the binary tree `[4,2,5,1,3]` where the nodes have the following structure:
```
    4
   / \
  2   5
 / \
1   3
```
The inorder traversal is `[1,2,3,4,5]`. The binary tree node is defined as `struct TreeNode { int val; TreeNode *left; TreeNode *right; TreeNode() : val(0), left(nullptr), right(nullptr) {} ; TreeNode(int x) : val(x), left(nullptr), right(nullptr) {} ; TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {} ; };`.

## Approach
The algorithm uses a recursive approach to traverse the binary tree, first visiting the left subtree, then the current node, and finally the right subtree. This can also be achieved iteratively using a stack to store nodes.

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
        traverse(root, result);
        return result;
    }
    
    void traverse(TreeNode* node, vector<int>& result) {
        if (node == nullptr) return;
        traverse(node->left, result);
        result.push_back(node->val);
        traverse(node->right, result);
    }
};
```

## Test Cases
```
Input: [4,2,5,1,3]
Output: [1,2,3,4,5]
Input: [1]
Output: [1]
Input: []
Output: []
```

## Key Takeaways
- Inorder traversal visits nodes in ascending order for a binary search tree.
- Recursive and iterative approaches can be used to solve this problem.
- The time complexity of both approaches is O(n), where n is the number of nodes in the tree.