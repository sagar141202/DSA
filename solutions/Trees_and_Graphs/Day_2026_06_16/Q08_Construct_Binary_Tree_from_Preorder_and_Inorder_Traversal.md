# Construct Binary Tree from Preorder and Inorder Traversal

## Problem Statement
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree. The length of both preorder and inorder will be the same, and the values in both arrays will be unique. The tree should be constructed in such a way that the preorder traversal of the resulting tree is the same as the given preorder array, and the inorder traversal is the same as the given inorder array.

## Approach
The approach involves recursively constructing the binary tree by identifying the root node from the preorder traversal and then finding its position in the inorder traversal to determine the left and right subtrees. We use a recursive function to build the tree, utilizing the preorder and inorder arrays.

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
        // Base case
        if (preorder.empty() || inorder.empty()) {
            return NULL;
        }
        
        // The first element of preorder is the root
        int rootVal = preorder[0];
        TreeNode* root = new TreeNode(rootVal);
        
        // Find the position of the root in inorder
        int rootIndex = -1;
        for (int i = 0; i < inorder.size(); i++) {
            if (inorder[i] == rootVal) {
                rootIndex = i;
                break;
            }
        }
        
        // Recursively construct the left and right subtrees
        vector<int> leftPreorder(preorder.begin() + 1, preorder.begin() + rootIndex + 1);
        vector<int> rightPreorder(preorder.begin() + rootIndex + 1, preorder.end());
        vector<int> leftInorder(inorder.begin(), inorder.begin() + rootIndex);
        vector<int> rightInorder(inorder.begin() + rootIndex + 1, inorder.end());
        
        root->left = buildTree(leftPreorder, leftInorder);
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
- The root of the tree is always the first element in the preorder traversal.
- The position of the root in the inorder traversal helps to identify the left and right subtrees.
- Recursive function calls are used to construct the left and right subtrees based on the preorder and inorder arrays.