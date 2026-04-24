# Construct Binary Tree from Preorder and Inorder Traversal

## Problem Statement
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree. The length of both preorder and inorder is n, and the values in both arrays are unique. The tree's nodes are numbered from 0 to n - 1. The nodes have no value, and the nodes' values will be the index of the node in the preorder array. The root of the tree is the first element in the preorder array, and the left and right subtrees of the root are the subtrees formed by the elements in the inorder array that are to the left and right of the root, respectively.

## Approach
The approach to solve this problem is to use recursion and a hash map to store the indices of the elements in the inorder array. We start by finding the root of the tree from the preorder array, then find its index in the inorder array. We recursively construct the left and right subtrees based on the indices.

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
        // Create a hash map to store the indices of the elements in the inorder array
        unordered_map<int, int> inorderIndex;
        for (int i = 0; i < inorder.size(); i++) {
            inorderIndex[inorder[i]] = i;
        }
        
        // Start the recursion with the entire preorder and inorder arrays
        return buildTree(preorder, 0, preorder.size() - 1, inorder, 0, inorder.size() - 1, inorderIndex);
    }
    
    TreeNode* buildTree(vector<int>& preorder, int preStart, int preEnd, vector<int>& inorder, int inStart, int inEnd, unordered_map<int, int>& inorderIndex) {
        // Base case: if the start index is greater than the end index, return null
        if (preStart > preEnd) {
            return nullptr;
        }
        
        // Create a new tree node with the current element from the preorder array
        TreeNode* root = new TreeNode(preorder[preStart]);
        
        // Find the index of the current element in the inorder array
        int inIndex = inorderIndex[preorder[preStart]];
        
        // Calculate the number of elements in the left subtree
        int leftSize = inIndex - inStart;
        
        // Recursively construct the left subtree
        root->left = buildTree(preorder, preStart + 1, preStart + leftSize, inorder, inStart, inIndex - 1, inorderIndex);
        
        // Recursively construct the right subtree
        root->right = buildTree(preorder, preStart + leftSize + 1, preEnd, inorder, inIndex + 1, inEnd, inorderIndex);
        
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
- Use recursion to construct the binary tree from preorder and inorder traversals.
- Utilize a hash map to store the indices of the elements in the inorder array for efficient lookup.
- Calculate the size of the left subtree based on the index of the current element in the inorder array.