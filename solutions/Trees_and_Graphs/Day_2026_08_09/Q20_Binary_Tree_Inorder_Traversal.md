# Binary Tree Inorder Traversal

## Problem Statement
Given the root of a binary tree, return the inorder traversal of its nodes' values. Inorder traversal visits the left subtree, then the current node, and finally the right subtree. For example, given the following binary tree: 
       4
     /   \
    2     5
   / \   / \
  1   3 6   7
The inorder traversal is: [1, 2, 3, 4, 5, 6, 7]. You can assume that all the values in the tree are unique.

## Approach
The algorithm uses a recursive approach to traverse the tree in inorder. It first visits the left subtree, then the current node, and finally the right subtree. This can also be implemented using a stack for iterative solution.

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
        if (node == nullptr) {
            return;
        }
        // Visit left subtree
        traverse(node->left, result);
        // Visit current node
        result.push_back(node->val);
        // Visit right subtree
        traverse(node->right, result);
    }
};
```

## Test Cases
```
Input: [4,2,5,1,3,6,7]
Output: [1,2,3,4,5,6,7]
Input: [1]
Output: [1]
Input: []
Output: []
```

## Key Takeaways
- Inorder traversal visits the left subtree, then the current node, and finally the right subtree.
- Recursive approach can be used to solve this problem.
- Iterative solution using a stack can also be implemented for this problem.