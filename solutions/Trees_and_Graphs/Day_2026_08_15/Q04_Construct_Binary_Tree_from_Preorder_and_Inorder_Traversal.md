# Construct Binary Tree from Preorder and Inorder Traversal

## Problem Statement
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree. The length of both arrays is equal to the number of nodes in the tree. The nodes are labeled from 0 to n - 1. The tree is guaranteed to be valid, and the preorder and inorder traversals are valid for a binary tree. For example, given preorder = [3,9,20,15,7] and inorder = [9,3,15,20,7], return the binary tree:
```
    3
   / \
  9  20
    /  \
   15   7
```
Constraints: 
- The number of nodes in the tree is equal to the length of both arrays.
- 1 <= preorder.length == inorder.length <= 30
- -100 <= preorder[i], inorder[i] <= 100
- The values in the arrays are unique.

## Approach
We can solve this problem by using recursion to construct the binary tree. We start by finding the root node from the preorder traversal, then find its position in the inorder traversal to determine the left and right subtrees.

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
        int rootVal = preorder[0];
        TreeNode* root = new TreeNode(rootVal);
        
        // Find the index of the root in inorder
        int index = -1;
        for (int i = 0; i < inorder.size(); i++) {
            if (inorder[i] == rootVal) {
                index = i;
                break;
            }
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
- The preorder traversal visits the root node first, then the left subtree, and finally the right subtree.
- The inorder traversal visits the left subtree, then the root node, and finally the right subtree.
- By combining these two traversals, we can uniquely construct a binary tree.