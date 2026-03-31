# Construct Binary Tree from Preorder and Inorder Traversal

## Problem Statement
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree. The length of both preorder and inorder is n, and the values in both arrays are distinct. The preorder array contains the values in the order they were visited during the preorder traversal (root, left, right), while the inorder array contains the values in the order they were visited during the inorder traversal (left, root, right). For example, given preorder = [3,9,20,15,7] and inorder = [9,3,15,20,7], return the binary tree represented by the arrays.

## Approach
To solve this problem, we can use recursion to construct the binary tree. We start by finding the root node from the preorder array, then find its index in the inorder array to determine the left and right subtrees. We recursively apply this process to construct the entire binary tree.

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
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        if (preorder.empty() || inorder.empty()) {
            return nullptr;
        }
        
        // Find the root node from the preorder array
        int rootVal = preorder[0];
        
        // Find the index of the root node in the inorder array
        int index = -1;
        for (int i = 0; i < inorder.size(); i++) {
            if (inorder[i] == rootVal) {
                index = i;
                break;
            }
        }
        
        // Create the root node
        TreeNode* root = new TreeNode(rootVal);
        
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
Output: [3,9,20,null,null,15,7]
```

## Key Takeaways
- The preorder array contains the values in the order they were visited during the preorder traversal (root, left, right).
- The inorder array contains the values in the order they were visited during the inorder traversal (left, root, right).
- We can use recursion to construct the binary tree by finding the root node and its index in the inorder array to determine the left and right subtrees.