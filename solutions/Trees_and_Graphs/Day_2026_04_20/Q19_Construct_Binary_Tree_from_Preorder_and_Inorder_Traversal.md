# Construct Binary Tree from Preorder and Inorder Traversal

## Problem Statement
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree. The length of both preorder and inorder is n, and the values in both arrays are unique. The tree's nodes are numbered from 0 to n - 1. The problem can be solved by recursively constructing the left and right subtrees based on the given traversals. For example, given preorder = [3,9,20,15,7] and inorder = [9,3,15,20,7], the output should be a binary tree where 3 is the root, 9 is the left child of 3, and 20 is the right child of 3, with 15 and 7 as the left and right children of 20 respectively.

## Approach
The approach involves using the preorder traversal to determine the root of the tree and the inorder traversal to determine the left and right subtrees. We use recursion to construct the left and right subtrees. The base case for the recursion is when the subtree is empty.

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
        if (preorder.empty() || inorder.empty()) {
            return NULL;
        }
        
        // The first element in preorder is the root
        int rootVal = preorder[0];
        TreeNode* root = new TreeNode(rootVal);
        
        // Find the index of the root in inorder
        int index = 0;
        while (inorder[index] != rootVal) {
            index++;
        }
        
        // Recursively construct the left and right subtrees
        vector<int> leftPreorder(preorder.begin() + 1, preorder.begin() + index + 1);
        vector<int> leftInorder(inorder.begin(), inorder.begin() + index);
        root->left = buildTree(leftPreorder, leftInorder);
        
        vector<int> rightPreorder(preorder.begin() + index + 1, preorder.end());
        vector<int> rightInorder(inorder.begin() + index + 1, inorder.end());
        root->right = buildTree(rightPreorder, rightInorder);
        
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
- The preorder traversal can be used to determine the root of the tree.
- The inorder traversal can be used to determine the left and right subtrees.
- Recursion can be used to construct the left and right subtrees.