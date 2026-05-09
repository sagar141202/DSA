# Construct Binary Tree from Preorder and Inorder Traversal

## Problem Statement
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree. The length of both arrays will be the same, and the values in the arrays will be unique. The tree should be constructed in such a way that the preorder traversal of the resulting tree is the same as the given preorder array and the inorder traversal of the resulting tree is the same as the given inorder array.

## Approach
We will use recursion to construct the binary tree by selecting the root node from the preorder array and then finding its position in the inorder array to determine the left and right subtrees.

## Complexity
- Time: O(N)
- Space: O(N)

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
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        if (preorder.empty() || inorder.empty()) return nullptr;
        
        // Root node is the first element in preorder array
        TreeNode* root = new TreeNode(preorder[0]);
        
        // Find the position of the root node in inorder array
        int pos = find(inorder.begin(), inorder.end(), preorder[0]) - inorder.begin();
        
        // Recursively construct the left subtree
        vector<int> leftPreorder(preorder.begin() + 1, preorder.begin() + pos + 1);
        vector<int> leftInorder(inorder.begin(), inorder.begin() + pos);
        root->left = buildTree(leftPreorder, leftInorder);
        
        // Recursively construct the right subtree
        vector<int> rightPreorder(preorder.begin() + pos + 1, preorder.end());
        vector<int> rightInorder(inorder.begin() + pos + 1, inorder.end());
        root->right = buildTree(rightPreorder, rightInorder);
        
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
- The root node of the binary tree is the first element in the preorder array.
- The position of the root node in the inorder array determines the left and right subtrees.
- Recursion is used to construct the left and right subtrees.