# Construct Binary Tree from Preorder and Inorder Traversal

## Problem Statement
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree. Assume that the input arrays represent a valid binary tree and there are no duplicate values in the tree. For example, given preorder = [3,9,20,15,7] and inorder = [9,3,15,20,7], the output should be a binary tree where 3 is the root, 9 is the left child of 3, and 20 is the right child of 3, with 15 and 7 as the left and right children of 20 respectively.

## Approach
We will use a recursive approach to solve this problem. The first element in the preorder array will be the root of the tree. We can find the index of this root in the inorder array and use it to divide the inorder array into two parts: the left subtree and the right subtree. Then, we can recursively construct the left and right subtrees.

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
        
        // The first element in the preorder array is the root
        int rootVal = preorder[0];
        TreeNode* root = new TreeNode(rootVal);
        
        // Find the index of the root in the inorder array
        int index = 0;
        while (inorder[index] != rootVal) {
            index++;
        }
        
        // Divide the preorder and inorder arrays into two parts: left subtree and right subtree
        vector<int> leftPreorder(preorder.begin() + 1, preorder.begin() + index + 1);
        vector<int> rightPreorder(preorder.begin() + index + 1, preorder.end());
        vector<int> leftInorder(inorder.begin(), inorder.begin() + index);
        vector<int> rightInorder(inorder.begin() + index + 1, inorder.end());
        
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
- The preorder array can be used to determine the root of the tree and the order of the nodes.
- The inorder array can be used to divide the tree into left and right subtrees.
- Recursive approach can be used to construct the binary tree from preorder and inorder traversal.