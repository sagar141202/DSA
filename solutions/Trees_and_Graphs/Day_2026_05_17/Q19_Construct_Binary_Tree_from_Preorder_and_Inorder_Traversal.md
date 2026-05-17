# Construct Binary Tree from Preorder and Inorder Traversal

## Problem Statement
Given the preorder and inorder traversal of a binary tree, construct the binary tree. The preorder traversal is a sequence of node values where the first value is the root, then the left subtree, and finally the right subtree. The inorder traversal is a sequence of node values where the left subtree is visited first, then the root, and finally the right subtree. The input is two lists of integers representing the preorder and inorder traversal of a binary tree. The output is the root of the constructed binary tree. For example, given preorder = [3,9,20,15,7] and inorder = [9,3,15,20,7], the constructed binary tree is:
       3
      / \
     9  20
       /  \
      15   7

## Approach
The approach to solve this problem is to use recursion to construct the binary tree. We start by finding the root node from the preorder traversal, then find its position in the inorder traversal to determine the left and right subtrees.

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
        
        // The first element of preorder is the root
        TreeNode* root = new TreeNode(preorder[0]);
        
        // Find the index of the root in inorder
        int index = 0;
        while (inorder[index] != preorder[0]) index++;
        
        // Recursively construct the left and right subtrees
        vector<int> leftPreorder(preorder.begin() + 1, preorder.begin() + index + 1);
        vector<int> leftInorder(inorder.begin(), inorder.begin() + index);
        vector<int> rightPreorder(preorder.begin() + index + 1, preorder.end());
        vector<int> rightInorder(inorder.begin() + index + 1, inorder.end());
        
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
- The preorder traversal gives us the root node, and the inorder traversal helps us to find the left and right subtrees.
- We use recursion to construct the binary tree.
- The time complexity is O(n) because we visit each node once, and the space complexity is O(n) due to the recursive call stack.