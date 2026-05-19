# Symmetric Tree

## Problem Statement
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center). A binary tree is symmetric if it is the same when its left subtree is a mirror reflection of its right subtree. For example, the tree with the following structure is symmetric: 
     1
   /   \
  2     2
 / \   / \
3   4 4   3
However, the following tree is not symmetric:
     1
   /   \
  2     2
   \   /
   3  4
The tree has at most 100 nodes, and each node has a unique value.

## Approach
To determine if a binary tree is symmetric, we can compare its left and right subtrees. We'll use a recursive approach to check if the left subtree is a mirror of the right subtree. This involves checking if the values of the nodes are equal and if the left child of the left subtree is a mirror of the right child of the right subtree.

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
    bool isSymmetric(TreeNode* root) {
        if (root == NULL) return true;
        return isMirror(root->left, root->right);
    }

    bool isMirror(TreeNode* left, TreeNode* right) {
        if (left == NULL && right == NULL) return true;
        if (left == NULL || right == NULL) return false;
        return (left->val == right->val) && isMirror(left->right, right->left) && isMirror(left->left, right->right);
    }
};
```

## Test Cases
```
Input: [1,2,2,3,4,4,3]
Output: true
Input: [1,2,2,null,3,null,3]
Output: false
```

## Key Takeaways
- Use recursion to compare the left and right subtrees of the binary tree.
- Check if the values of the nodes are equal and if the left child of the left subtree is a mirror of the right child of the right subtree.
- Handle the base cases where the trees are NULL or empty.