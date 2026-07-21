# Construct Binary Tree from Preorder and Inorder Traversal

## Problem Statement
Given the preorder and inorder traversal of a binary tree, construct the binary tree. The preorder traversal visits the root node first, then recursively traverses the left subtree, and finally the right subtree. The inorder traversal visits the left subtree, then the root node, and finally the right subtree. The problem assumes that the input trees do not contain duplicate values.

## Approach
We can solve this problem by recursively constructing the binary tree. The preorder traversal gives us the root node, and the inorder traversal helps us to determine the left and right subtrees. By finding the index of the root node in the inorder traversal, we can split the inorder traversal into left and right subtrees.

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
        
        // The first element in the preorder traversal is the root
        int rootVal = preorder[0];
        TreeNode* root = new TreeNode(rootVal);
        
        // Find the index of the root in the inorder traversal
        int rootIndex = -1;
        for (int i = 0; i < inorder.size(); i++) {
            if (inorder[i] == rootVal) {
                rootIndex = i;
                break;
            }
        }
        
        // Split the inorder traversal into left and right subtrees
        vector<int> leftInorder(inorder.begin(), inorder.begin() + rootIndex);
        vector<int> rightInorder(inorder.begin() + rootIndex + 1, inorder.end());
        
        // Split the preorder traversal into left and right subtrees
        vector<int> leftPreorder(preorder.begin() + 1, preorder.begin() + 1 + leftInorder.size());
        vector<int> rightPreorder(preorder.begin() + 1 + leftInorder.size(), preorder.end());
        
        // Recursively construct the left and right subtrees
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
- The preorder traversal gives us the root node, and the inorder traversal helps us to determine the left and right subtrees.
- By finding the index of the root node in the inorder traversal, we can split the inorder traversal into left and right subtrees.
- We can recursively construct the binary tree by splitting the preorder and inorder traversals into left and right subtrees.