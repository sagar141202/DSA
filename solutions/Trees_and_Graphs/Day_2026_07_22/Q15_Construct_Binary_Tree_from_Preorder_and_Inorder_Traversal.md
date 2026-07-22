# Construct Binary Tree from Preorder and Inorder Traversal

## Problem Statement
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree. The length of both preorder and inorder is n, and the values in both arrays are distinct. The tree's nodes are numbered from 0 to n - 1. The nodes' values are given by the arrays' values. The root of the tree is the first element in the preorder array, and the left and right subtrees of the root are constructed recursively.

## Approach
We can solve this problem by recursively constructing the binary tree. We start with the root node, which is the first element in the preorder array, and then recursively construct the left and right subtrees. The base case is when the preorder and inorder arrays are empty.

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
        
        // The first element in preorder is the root
        TreeNode* root = new TreeNode(preorder[0]);
        
        // Find the index of the root in inorder
        int index = 0;
        while (inorder[index] != preorder[0]) index++;
        
        // Recursively construct the left and right subtrees
        vector<int> leftPreorder(preorder.begin() + 1, preorder.begin() + index + 1);
        vector<int> rightPreorder(preorder.begin() + index + 1, preorder.end());
        vector<int> leftInorder(inorder.begin(), inorder.begin() + index);
        vector<int> rightInorder(inorder.begin() + index + 1, inorder.end());
        
        root->left = buildTree(leftPreorder, leftInorder);
        root->right = buildTree(rightPreorder, rightInorder);
        
        return root;
    }
};
```

## Test Cases
```
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,15,7]
```

## Key Takeaways
- The preorder traversal visits the root node first, then recursively traverses the left subtree, and finally the right subtree.
- The inorder traversal visits the left subtree, then the root node, and finally the right subtree.
- By combining these two traversals, we can uniquely determine the structure of the binary tree.