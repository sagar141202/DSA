# Binary Tree Inorder Traversal

## Problem Statement
Given the root of a binary tree, return the inorder traversal of its nodes' values. Inorder traversal visits the left subtree, the current node, and then the right subtree. The function should take the root of the binary tree as input and return a vector of integers representing the inorder traversal. For example, given the binary tree `[4,2,5,1,3]`, the function should return `[1,2,3,4,5]`. The binary tree is defined as follows: each node has a unique value, and for each node, all elements in its left subtree are less than the node, and all elements in its right subtree are greater than the node.

## Approach
The algorithm uses a recursive approach to traverse the binary tree in inorder. It first visits the left subtree, then the current node, and finally the right subtree. This can also be achieved using an iterative approach with a stack.

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
- The algorithm can be implemented using both recursive and iterative approaches.
- The time complexity is O(n), where n is the number of nodes in the binary tree, and the space complexity is O(n) due to the recursive call stack or the explicit stack used in the iterative approach.