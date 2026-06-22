# Construct Binary Tree from Preorder and Inorder Traversal

## Problem Statement
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree. The length of both preorder and inorder arrays is n, and the values in both arrays are distinct. The preorder array is given by [root, left, right] and the inorder array is given by [left, root, right]. For example, given preorder = [3,9,20,15,7] and inorder = [9,3,15,20,7], return the binary tree root node where the tree is:
```
    3
   / \
  9  20
    /  \
   15   7
```

## Approach
We use a recursive approach to construct the binary tree, using the preorder array to determine the root node and the inorder array to determine the left and right subtrees. We find the index of the root in the inorder array, and then recursively construct the left and right subtrees.

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
        int rootVal = preorder[0];
        TreeNode* root = new TreeNode(rootVal);
        int index = 0;
        // Find the index of the root in the inorder array
        while (index < inorder.size() && inorder[index] != rootVal) {
            index++;
        }
        // Construct the left subtree
        vector<int> leftPreorder(preorder.begin() + 1, preorder.begin() + index + 1);
        vector<int> leftInorder(inorder.begin(), inorder.begin() + index);
        root->left = buildTree(leftPreorder, leftInorder);
        // Construct the right subtree
        vector<int> rightPreorder(preorder.begin() + index + 1, preorder.end());
        vector<int> rightInorder(inorder.begin() + index + 1, inorder.end());
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
- Use the preorder array to determine the root node and the inorder array to determine the left and right subtrees.
- Find the index of the root in the inorder array to split the arrays for the left and right subtrees.
- Recursively construct the left and right subtrees using the same approach.