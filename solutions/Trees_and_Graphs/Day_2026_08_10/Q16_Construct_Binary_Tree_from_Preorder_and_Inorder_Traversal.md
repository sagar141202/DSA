# Construct Binary Tree from Preorder and Inorder Traversal

## Problem Statement
Given the preorder and inorder traversal of a binary tree, construct the binary tree. The preorder traversal visits the root node first, then recursively traverses the left subtree, and finally the right subtree. The inorder traversal visits the left subtree, then the root node, and finally the right subtree. The input arrays are 1-indexed and 0-indexed respectively, with values representing node values. For example, given preorder = [3,9,20,15,7] and inorder = [9,3,15,20,7], the output should be a binary tree where 3 is the root, 9 is the left child of 3, and 20 is the right child of 3, with 15 and 7 as the left and right children of 20 respectively.

## Approach
We can use recursion to solve this problem by selecting the root node from the preorder traversal and finding its index in the inorder traversal. This allows us to determine the left and right subtrees and recursively construct them. The base case is when the input arrays are empty.

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
        TreeNode* root = new TreeNode(preorder[0]);
        int index = find(inorder.begin(), inorder.end(), preorder[0]) - inorder.begin();
        vector<int> left_inorder(inorder.begin(), inorder.begin() + index);
        vector<int> right_inorder(inorder.begin() + index + 1, inorder.end());
        vector<int> left_preorder(preorder.begin() + 1, preorder.begin() + index + 1);
        vector<int> right_preorder(preorder.begin() + index + 1, preorder.end());
        root->left = buildTree(left_preorder, left_inorder);
        root->right = buildTree(right_preorder, right_inorder);
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
- The problem can be solved using recursion by selecting the root node from the preorder traversal and finding its index in the inorder traversal.
- The time complexity is O(n) because we visit each node once, where n is the number of nodes in the tree.
- The space complexity is O(n) due to the recursive call stack and the storage of the output tree.