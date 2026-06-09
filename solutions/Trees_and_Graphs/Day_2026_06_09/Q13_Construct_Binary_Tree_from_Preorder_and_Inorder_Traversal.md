# Construct Binary Tree from Preorder and Inorder Traversal

## Problem Statement
Given the preorder and inorder traversal sequences of a binary tree, reconstruct the binary tree. The preorder traversal visits the root node first, then recursively traverses the left subtree, and finally the right subtree. The inorder traversal visits the left subtree, then the root node, and finally the right subtree. Assume that the input sequences do not contain duplicate values.

## Approach
We use recursion to construct the binary tree. The first element in the preorder sequence is the root, and we find its position in the inorder sequence to determine the left and right subtrees. We then recursively construct the left and right subtrees.

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
        
        // Find the position of the root in inorder
        int pos = 0;
        while (inorder[pos] != rootVal) {
            pos++;
        }
        
        // Construct the left subtree
        vector<int> leftPreorder(preorder.begin() + 1, preorder.begin() + pos + 1);
        vector<int> leftInorder(inorder.begin(), inorder.begin() + pos);
        root->left = buildTree(leftPreorder, leftInorder);
        
        // Construct the right subtree
        vector<int> rightPreorder(preorder.begin() + pos + 1, preorder.end());
        vector<int> rightInorder(inorder.begin() + pos + 1, inorder.end());
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
- The first element in the preorder sequence is the root of the binary tree.
- The position of the root in the inorder sequence determines the left and right subtrees.
- Recursion is used to construct the left and right subtrees.