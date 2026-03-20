# Construct Binary Tree from Preorder and Inorder Traversal

## Problem Statement
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree. The length of both preorder and inorder is n. The values in the arrays are distinct. The preorder array contains the values in the order they were visited during the preorder traversal (root, left, right), and the inorder array contains the values in the order they were visited during the inorder traversal (left, root, right). For example, given preorder = [3,9,20,15,7] and inorder = [9,3,15,20,7], return the binary tree:
```
    3
   / \
  9  20
    /  \
   15   7
```

## Approach
We use a recursive approach to construct the binary tree. The first element in the preorder array is the root of the tree, and we find its index in the inorder array to determine the left and right subtrees. We then recursively construct the left and right subtrees.

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
Output: 
    3
   / \
  9  20
    /  \
   15   7
```

## Key Takeaways
- The first element in the preorder array is the root of the tree.
- The index of the root in the inorder array determines the left and right subtrees.
- We recursively construct the left and right subtrees using the corresponding elements in the preorder and inorder arrays.