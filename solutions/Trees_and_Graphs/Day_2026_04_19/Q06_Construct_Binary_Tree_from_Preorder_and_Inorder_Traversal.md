# Construct Binary Tree from Preorder and Inorder Traversal

## Problem Statement
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree. The length of both preorder and inorder is n, and the values in both arrays are distinct. The preorder traversal visits the root node first, then traverses the left subtree, and finally traverses the right subtree. The inorder traversal visits the left subtree, then the root node, and finally the right subtree.

## Approach
We can use a recursive approach to solve this problem by finding the root node in the inorder traversal and then recursively constructing the left and right subtrees. The preorder traversal provides the root node, and the inorder traversal helps us find the boundary between the left and right subtrees.

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
        // base case
        if (preorder.empty() || inorder.empty()) {
            return NULL;
        }
        
        // find the root node
        int rootVal = preorder[0];
        TreeNode* root = new TreeNode(rootVal);
        
        // find the index of the root node in the inorder traversal
        int rootIndex = -1;
        for (int i = 0; i < inorder.size(); i++) {
            if (inorder[i] == rootVal) {
                rootIndex = i;
                break;
            }
        }
        
        // recursively construct the left subtree
        vector<int> leftPreorder(preorder.begin() + 1, preorder.begin() + rootIndex + 1);
        vector<int> leftInorder(inorder.begin(), inorder.begin() + rootIndex);
        root->left = buildTree(leftPreorder, leftInorder);
        
        // recursively construct the right subtree
        vector<int> rightPreorder(preorder.begin() + rootIndex + 1, preorder.end());
        vector<int> rightInorder(inorder.begin() + rootIndex + 1, inorder.end());
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
- The preorder traversal provides the root node, and the inorder traversal helps us find the boundary between the left and right subtrees.
- We can use a recursive approach to solve this problem by finding the root node in the inorder traversal and then recursively constructing the left and right subtrees.
- The time complexity is O(n) because we visit each node once, and the space complexity is O(n) due to the recursive call stack.