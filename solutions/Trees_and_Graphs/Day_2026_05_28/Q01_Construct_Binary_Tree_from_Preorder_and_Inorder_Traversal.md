# Construct Binary Tree from Preorder and Inorder Traversal

## Problem Statement
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree. The length of both preorder and inorder arrays is n, and the values in both arrays are distinct. The preorder traversal of a binary tree is a traversal where the root node is visited first, then the left subtree, and finally the right subtree. The inorder traversal of a binary tree is a traversal where the left subtree is visited first, then the root node, and finally the right subtree.

## Approach
We use a recursive approach to construct the binary tree, where we first find the root node from the preorder array, then find its position in the inorder array to determine the left and right subtrees. We recursively apply this process to build the entire tree.

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
        // Base case: if the input arrays are empty, return NULL
        if (preorder.empty() || inorder.empty()) {
            return NULL;
        }
        
        // Find the root node from the preorder array
        int rootVal = preorder[0];
        TreeNode* root = new TreeNode(rootVal);
        
        // Find the position of the root node in the inorder array
        int rootIndex = -1;
        for (int i = 0; i < inorder.size(); i++) {
            if (inorder[i] == rootVal) {
                rootIndex = i;
                break;
            }
        }
        
        // Recursively build the left and right subtrees
        vector<int> leftPreorder(preorder.begin() + 1, preorder.begin() + rootIndex + 1);
        vector<int> leftInorder(inorder.begin(), inorder.begin() + rootIndex);
        vector<int> rightPreorder(preorder.begin() + rootIndex + 1, preorder.end());
        vector<int> rightInorder(inorder.begin() + rootIndex + 1, inorder.end());
        
        root->left = buildTree(leftPreorder, leftInorder);
        root->right = buildTree(rightPreorder, rightInorder);
        
        return root;
    }
};
```

## Test Cases
```
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,15,7]
```

## Key Takeaways
- The preorder traversal visits the root node first, which helps us identify the root node in the tree.
- The inorder traversal visits the left subtree first, which helps us determine the left and right subtrees of the root node.
- Recursive approach is suitable for this problem, as it allows us to break down the problem into smaller sub-problems and solve them independently.