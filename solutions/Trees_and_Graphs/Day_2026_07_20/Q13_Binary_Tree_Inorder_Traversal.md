# Binary Tree Inorder Traversal

## Problem Statement
Given the root of a binary tree, return the inorder traversal of its nodes' values. Inorder traversal visits the left subtree, then the current node, and finally the right subtree. For example, given the binary tree `[4,2,5,1,3]` where the nodes have the following structure:
        4
       / \
      2   5
     / \
    1   3
The inorder traversal is `[1,2,3,4,5]`. The function should take the root of the binary tree as input and return a vector of integers representing the inorder traversal.

## Approach
The algorithm uses a recursive approach to traverse the binary tree in inorder. It first visits the left subtree, then the current node, and finally the right subtree. This ensures that the nodes are visited in the correct order.

## Complexity
- Time: O(n)
- Space: O(h)

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
        helper(root, result);
        return result;
    }
    
    void helper(TreeNode* node, vector<int>& result) {
        if (node == NULL) return;
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
- Inorder traversal visits the left subtree, then the current node, and finally the right subtree.
- The recursive approach ensures that the nodes are visited in the correct order.
- The time complexity is O(n) where n is the number of nodes in the binary tree, and the space complexity is O(h) where h is the height of the binary tree.