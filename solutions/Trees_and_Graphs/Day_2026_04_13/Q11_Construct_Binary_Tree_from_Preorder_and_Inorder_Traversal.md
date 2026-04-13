# Construct Binary Tree from Preorder and Inorder Traversal

## Problem Statement
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree. The length of both preorder and inorder is n, and the values in both arrays are unique. The tree's nodes are numbered from 0 to n - 1, and the values of the nodes are the same as the values in the preorder array. The problem can be solved using recursion and a hashmap to store the indices of the inorder array.

## Approach
The approach involves using recursion to construct the binary tree. We start by finding the root node from the preorder array, then find its index in the inorder array. We then recursively construct the left and right subtrees.

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
        // Create a hashmap to store the indices of the inorder array
        unordered_map<int, int> inorderMap;
        for (int i = 0; i < inorder.size(); i++) {
            inorderMap[inorder[i]] = i;
        }
        return buildTreeHelper(preorder, 0, preorder.size() - 1, inorder, 0, inorder.size() - 1, inorderMap);
    }

    TreeNode* buildTreeHelper(vector<int>& preorder, int preStart, int preEnd, vector<int>& inorder, int inStart, int inEnd, unordered_map<int, int>& inorderMap) {
        if (preStart > preEnd || inStart > inEnd) return NULL;
        // Create the root node
        TreeNode* root = new TreeNode(preorder[preStart]);
        // Find the index of the root node in the inorder array
        int inIndex = inorderMap[preorder[preStart]];
        // Calculate the number of nodes in the left subtree
        int leftSize = inIndex - inStart;
        // Recursively construct the left subtree
        root->left = buildTreeHelper(preorder, preStart + 1, preStart + leftSize, inorder, inStart, inIndex - 1, inorderMap);
        // Recursively construct the right subtree
        root->right = buildTreeHelper(preorder, preStart + leftSize + 1, preEnd, inorder, inIndex + 1, inEnd, inorderMap);
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
- The problem can be solved using recursion and a hashmap to store the indices of the inorder array.
- The time complexity is O(n) where n is the number of nodes in the tree.
- The space complexity is O(n) where n is the number of nodes in the tree.