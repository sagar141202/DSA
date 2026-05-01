# Construct Binary Tree from Preorder and Inorder Traversal

## Problem Statement
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree. The length of both preorder and inorder is n, and the values in both arrays are unique. The tree should be constructed in a way that the preorder traversal of the resulting tree is the same as the given preorder array, and the inorder traversal of the resulting tree is the same as the given inorder array.

## Approach
The approach to solve this problem involves using recursion to construct the binary tree. We can use the preorder array to determine the root of the tree and the inorder array to determine the left and right subtrees. By finding the index of the root in the inorder array, we can split the array into left and right subtrees and recursively construct them.

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
        // Base case: if the preorder array is empty, return NULL
        if (preorder.empty()) {
            return NULL;
        }
        
        // The first element in the preorder array is the root
        int rootVal = preorder[0];
        TreeNode* root = new TreeNode(rootVal);
        
        // Find the index of the root in the inorder array
        int rootIndex = -1;
        for (int i = 0; i < inorder.size(); i++) {
            if (inorder[i] == rootVal) {
                rootIndex = i;
                break;
            }
        }
        
        // Split the inorder array into left and right subtrees
        vector<int> leftInorder(inorder.begin(), inorder.begin() + rootIndex);
        vector<int> rightInorder(inorder.begin() + rootIndex + 1, inorder.end());
        
        // Split the preorder array into left and right subtrees
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
Output: [3,9,20,null,null,15,7]
```

## Key Takeaways
- The preorder array can be used to determine the root of the tree.
- The inorder array can be used to determine the left and right subtrees.
- Recursion can be used to construct the binary tree by splitting the arrays into left and right subtrees.