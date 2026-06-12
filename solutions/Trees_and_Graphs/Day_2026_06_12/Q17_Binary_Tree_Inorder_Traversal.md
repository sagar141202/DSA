# Binary Tree Inorder Traversal

## Problem Statement
Given the root of a binary tree, return the inorder traversal of its nodes' values. Inorder traversal visits the left subtree, the current node, and then the right subtree. For example, given the binary tree `[4,2,5,1,3]`, the inorder traversal is `[1,2,3,4,5]`. The binary tree node is defined as `struct TreeNode { int val; TreeNode *left; TreeNode *right; TreeNode(int x) : val(x), left(NULL), right(NULL) {} };`. The function should return a vector of integers representing the inorder traversal of the binary tree.

## Approach
The algorithm uses a recursive approach to traverse the binary tree in inorder. It first visits the left subtree, then the current node, and finally the right subtree. This can also be achieved using an iterative approach with a stack to store nodes.

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
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> result;
        traverse(root, result);
        return result;
    }
    
    void traverse(TreeNode* node, vector<int>& result) {
        if (node == NULL) return;
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
- Inorder traversal visits the left subtree, the current node, and then the right subtree.
- The recursive approach is simple to implement but may cause a stack overflow for very large trees.
- The iterative approach with a stack can avoid the recursive function call overhead and is suitable for very large trees.