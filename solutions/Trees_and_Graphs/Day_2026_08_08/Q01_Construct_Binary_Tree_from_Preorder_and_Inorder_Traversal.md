# Construct Binary Tree from Preorder and Inorder Traversal

## Problem Statement
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree. The length of both preorder and inorder arrays will be the same, and each element will be unique. The preorder array will contain the root node first, then the left subtree, and finally the right subtree. The inorder array will contain the left subtree, then the root node, and finally the right subtree. For example, given preorder = [3,9,20,15,7] and inorder = [9,3,15,20,7], return the binary tree whose preorder traversal is [3,9,20,15,7] and inorder traversal is [9,3,15,20,7].

## Approach
We can solve this problem by using a recursive approach, where we first find the root node from the preorder array, then find the left and right subtrees from the inorder array. We use the index of the root node in the inorder array to split the inorder array into left and right subtrees.

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
- Use recursive approach to construct the binary tree.
- Find the root node from the preorder array and split the inorder array into left and right subtrees.
- Use the index of the root node in the inorder array to split the preorder array into left and right subtrees.