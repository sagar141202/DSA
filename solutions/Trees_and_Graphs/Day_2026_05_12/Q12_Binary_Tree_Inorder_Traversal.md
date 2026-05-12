# Binary Tree Inorder Traversal

## Problem Statement
Given the root of a binary tree, return the inorder traversal of its nodes' values. Inorder traversal visits the left subtree, the current node, and then the right subtree. For example, given the binary tree `[4,2,5,1,3]`, the inorder traversal is `[1,2,3,4,5]`. The binary tree node has the following structure: `TreeNode(val=0, left=None, right=None)`. The function should take the root of the binary tree as input and return a vector of integers representing the inorder traversal.

## Approach
The algorithm uses a recursive approach to traverse the binary tree in inorder. It first visits the left subtree, then the current node, and finally the right subtree. This can be achieved using a recursive function or an iterative approach using a stack.

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
        helper(root, result);
        return result;
    }
    
    void helper(TreeNode* node, vector<int>& result) {
        if (node == nullptr) return;
        helper(node->left, result);
        result.push_back(node->val);
        helper(node->right, result);
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
- The inorder traversal visits the left subtree, the current node, and then the right subtree.
- The time complexity is O(n), where n is the number of nodes in the binary tree, since we visit each node exactly once.
- The space complexity is O(n), where n is the number of nodes in the binary tree, due to the recursive call stack or the explicit stack used in the iterative approach.