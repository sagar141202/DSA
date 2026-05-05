# Construct Binary Tree from Preorder and Inorder Traversal

## Problem Statement
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree. The length of both preorder and inorder is n, and the values in both arrays are distinct. The preorder traversal of a binary tree is a traversal where the parent node is visited before its child nodes, and the inorder traversal of a binary tree is a traversal where the left child node is visited before its parent node, and the parent node is visited before its right child node.

## Approach
The approach is to use recursion to construct the binary tree. We start by finding the root node in the inorder traversal, then recursively construct the left and right subtrees.

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
            return nullptr;
        }
        // The root node is the first node in the preorder traversal
        TreeNode* root = new TreeNode(preorder[0]);
        // Find the index of the root node in the inorder traversal
        int index = find(inorder.begin(), inorder.end(), preorder[0]) - inorder.begin();
        // Recursively construct the left subtree
        vector<int> leftPreorder(preorder.begin() + 1, preorder.begin() + index + 1);
        vector<int> leftInorder(inorder.begin(), inorder.begin() + index);
        root->left = buildTree(leftPreorder, leftInorder);
        // Recursively construct the right subtree
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
- The key to solving this problem is to find the root node in the inorder traversal and then recursively construct the left and right subtrees.
- The preorder traversal is used to determine the root node and the order of the nodes, while the inorder traversal is used to determine the structure of the tree.
- The time complexity is O(n) because we visit each node once, and the space complexity is O(n) because of the recursive call stack.