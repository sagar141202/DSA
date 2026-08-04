# Construct Binary Tree from Preorder and Inorder Traversal

## Problem Statement
Given the preorder and inorder traversal of a binary tree, construct the binary tree. The preorder traversal visits the root node first, then recursively traverses the left subtree, and finally the right subtree. The inorder traversal visits the left subtree, then the root node, and finally the right subtree. The problem assumes that the input trees do not contain duplicate values.

## Approach
We can solve this problem using recursion by selecting the root node from the preorder traversal and finding its position in the inorder traversal. This allows us to divide the problem into smaller sub-problems and construct the left and right subtrees.

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
        
        // The first element in the preorder traversal is the root node
        int rootVal = preorder[0];
        TreeNode* root = new TreeNode(rootVal);
        
        // Find the index of the root node in the inorder traversal
        int index = 0;
        while (inorder[index] != rootVal) index++;
        
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
- The preorder traversal provides the root node, while the inorder traversal helps to identify the left and right subtrees.
- Recursion is used to divide the problem into smaller sub-problems and construct the left and right subtrees.
- The time complexity is O(n), where n is the number of nodes in the tree, since we visit each node once.