# Construct Binary Tree from Preorder and Inorder Traversal

## Problem Statement
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree. The length of both arrays is equal to the number of nodes in the tree. It is guaranteed that the input arrays represent a valid binary tree. For example, given preorder = [3,9,20,15,7] and inorder = [9,3,15,20,7], return the binary tree represented by the arrays.

## Approach
The approach to solve this problem is to use recursion and divide the problem into smaller sub-problems. We will first find the root node from the preorder array, then find its position in the inorder array to divide the tree into left and right subtrees.

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
        
        // Root node is the first element in preorder array
        TreeNode* root = new TreeNode(preorder[0]);
        
        // Find the position of root node in inorder array
        int pos = 0;
        while (inorder[pos] != preorder[0]) pos++;
        
        // Recursively construct left and right subtrees
        vector<int> leftPreorder(preorder.begin() + 1, preorder.begin() + pos + 1);
        vector<int> leftInorder(inorder.begin(), inorder.begin() + pos);
        vector<int> rightPreorder(preorder.begin() + pos + 1, preorder.end());
        vector<int> rightInorder(inorder.begin() + pos + 1, inorder.end());
        
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
- The problem can be solved using recursion and divide-and-conquer approach.
- The root node is the first element in the preorder array.
- The position of the root node in the inorder array is used to divide the tree into left and right subtrees.