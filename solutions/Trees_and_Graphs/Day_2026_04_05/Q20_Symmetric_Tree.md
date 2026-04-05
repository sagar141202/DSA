# Symmetric Tree

## Problem Statement
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center). A binary tree is symmetric if it is the same when its left subtree is a mirror reflection of its right subtree. The tree only contains nodes with values 0-9. For example, the tree [1,2,2,null,3,null,3] is symmetric, but the tree [1,2,2,null,2,null,2] is not.

## Approach
To determine if a binary tree is symmetric, we can use a recursive approach to compare the left and right subtrees. We will check if the left subtree is a mirror of the right subtree by comparing the values of the nodes and their respective structures.

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
Input: [1,2,2,null,3,null,3]
Output: true

Input: [1,2,2,null,2,null,2]
Output: false
```

## Key Takeaways
- A binary tree is symmetric if its left subtree is a mirror reflection of its right subtree.
- We can use a recursive approach to compare the left and right subtrees.
- The time complexity is O(n), where n is the number of nodes in the tree, and the space complexity is O(h), where h is the height of the tree.