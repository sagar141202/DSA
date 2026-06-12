# Construct Binary Tree from Preorder and Inorder Traversal

## Problem Statement
Given the preorder and inorder traversal of a binary tree, construct the binary tree. The preorder traversal visits the root node first, then recursively traverses the left subtree, and finally the right subtree. The inorder traversal visits the left subtree, then the root node, and finally the right subtree. The input arrays are 1-indexed and 0-indexed in the code. For example, given preorder = [3,9,20,15,7] and inorder = [9,3,15,20,7], return the binary tree represented as a nested list, where each node is a list of three elements: the node's value, its left child, and its right child.

## Approach
We will use recursion to solve this problem, where we find the root node from the preorder traversal and then divide the inorder traversal into left and right subtrees. We then recursively construct the left and right subtrees.

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
        
        // Find the root node from the preorder traversal
        int rootVal = preorder[0];
        
        // Find the index of the root node in the inorder traversal
        int rootIndex = -1;
        for (int i = 0; i < inorder.size(); i++) {
            if (inorder[i] == rootVal) {
                rootIndex = i;
                break;
            }
        }
        
        // Create the root node
        TreeNode* root = new TreeNode(rootVal);
        
        // Divide the inorder traversal into left and right subtrees
        vector<int> leftInorder(inorder.begin(), inorder.begin() + rootIndex);
        vector<int> rightInorder(inorder.begin() + rootIndex + 1, inorder.end());
        
        // Divide the preorder traversal into left and right subtrees
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
- The root node can be found from the preorder traversal.
- The inorder traversal can be divided into left and right subtrees based on the root node.
- Recursion can be used to construct the left and right subtrees.