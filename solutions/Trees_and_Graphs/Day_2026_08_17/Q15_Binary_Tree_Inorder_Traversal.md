# Binary Tree Inorder Traversal

## Problem Statement
Given the root of a binary tree, return the inorder traversal of its nodes' values. Inorder traversal visits the left subtree, then the current node, and finally the right subtree. The binary tree node has the following definition: `struct TreeNode { int val; TreeNode *left; TreeNode *right; TreeNode() : val(0), left(nullptr), right(nullptr) {}; TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}; TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}; };`. For example, given the binary tree `[4,2,5,1,3]`, the inorder traversal is `[1,2,3,4,5]`. The input tree is guaranteed to have at most `100` nodes, and the values of the nodes are in the range `[0, 100]`.

## Approach
The algorithm uses a recursive or iterative approach to traverse the binary tree in an inorder manner. It first visits the left subtree, then the current node, and finally the right subtree. This ensures that the nodes are visited in ascending order.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
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
- Inorder traversal visits the left subtree, then the current node, and finally the right subtree.
- The time complexity of the solution is O(n), where n is the number of nodes in the binary tree.
- The space complexity of the solution is O(n) due to the recursive call stack or the explicit stack used in the iterative solution.