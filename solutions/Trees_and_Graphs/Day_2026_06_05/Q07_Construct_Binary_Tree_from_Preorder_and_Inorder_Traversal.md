# Construct Binary Tree from Preorder and Inorder Traversal

## Problem Statement
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree. The length of both preorder and inorder arrays will be the same, and each value in the arrays will be unique. The preorder array will contain the root node first, then the left subtree, and finally the right subtree. The inorder array will contain the left subtree, then the root node, and finally the right subtree. The size of the input arrays will be between 1 and 1000.

## Approach
We can solve this problem by recursively constructing the binary tree. We start by finding the root node in the inorder array, then recursively construct the left and right subtrees. The base case for the recursion is when the preorder or inorder array is empty.

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
        // Base case: if the preorder or inorder array is empty, return NULL
        if (preorder.empty() || inorder.empty()) {
            return NULL;
        }
        
        // Create a new TreeNode with the value of the first element in the preorder array
        TreeNode* root = new TreeNode(preorder[0]);
        
        // Find the index of the root node in the inorder array
        int index = find(inorder.begin(), inorder.end(), preorder[0]) - inorder.begin();
        
        // Recursively construct the left subtree
        vector<int> leftPreorder(preorder.begin() + 1, preorder.begin() + index + 1);
        vector<int> leftInorder(inorder.begin(), inorder.begin() + index);
        root->left = buildTree(leftPreorder, leftInorder);
        
        // Recursively construct the right subtree
        vector<int> rightPreorder(preorder.begin() + index + 1, preorder.end());
        vector<int> rightInorder(inorder.begin() + index + 1, inorder.end());
        root->right = buildTree(rightPreorder, rightInorder);
        
        // Return the root node
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
- The preorder array can be used to determine the root node of the binary tree.
- The inorder array can be used to determine the structure of the binary tree.
- Recursive functions can be used to construct the binary tree.