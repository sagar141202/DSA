# Construct Binary Tree from Preorder and Inorder Traversal

## Problem Statement
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree. The length of both preorder and inorder arrays will be the same, and each value in the arrays will be unique. The preorder array will contain the root node first, then the values in the left subtree, and finally the values in the right subtree. The inorder array will contain the values in the left subtree, then the root node, and finally the values in the right subtree.

## Approach
We can solve this problem by recursively constructing the binary tree. We start by finding the root node in the inorder array, then recursively construct the left and right subtrees.

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
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        if (preorder.empty() || inorder.empty()) return NULL;
        TreeNode* root = new TreeNode(preorder[0]);
        int index = find(inorder.begin(), inorder.end(), preorder[0]) - inorder.begin();
        vector<int> left_inorder(inorder.begin(), inorder.begin() + index);
        vector<int> right_inorder(inorder.begin() + index + 1, inorder.end());
        vector<int> left_preorder(preorder.begin() + 1, preorder.begin() + index + 1);
        vector<int> right_preorder(preorder.begin() + index + 1, preorder.end());
        root->left = buildTree(left_preorder, left_inorder);
        root->right = buildTree(right_preorder, right_inorder);
        return root;
    }
};
```

## Test Cases
```
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
```

## Key Takeaways
- The preorder array contains the root node first, then the left subtree, and finally the right subtree.
- The inorder array contains the left subtree, then the root node, and finally the right subtree.
- We can recursively construct the binary tree by finding the root node in the inorder array and then constructing the left and right subtrees.