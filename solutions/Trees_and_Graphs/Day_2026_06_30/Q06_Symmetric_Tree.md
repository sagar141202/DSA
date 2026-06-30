# Symmetric Tree

## Problem Statement
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center). A binary tree is symmetric if the left subtree is a mirror reflection of the right subtree. For example, the binary tree `[1,2,2,3,4,4,3]` is symmetric, but the binary tree `[1,2,2,null,3,null,3]` is not symmetric. The tree is empty if the root is null.

## Approach
We will use a recursive approach to check if the left subtree is a mirror of the right subtree. This can be done by checking if the left child of the left subtree is equal to the right child of the right subtree, and vice versa. We will also check if the values of the nodes are equal.

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
- To check if a binary tree is symmetric, we need to check if the left subtree is a mirror of the right subtree.
- We can use a recursive approach to check if the left subtree is a mirror of the right subtree.
- The time complexity of this approach is O(n), where n is the number of nodes in the tree, and the space complexity is O(h), where h is the height of the tree.