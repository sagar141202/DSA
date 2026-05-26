# Construct Binary Tree from Preorder and Inorder Traversal

## Problem Statement
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree. The length of both preorder and inorder is n, and the values in both arrays are unique. The tree is guaranteed to be valid, i.e., there will be no duplicate values in the tree. For example, given preorder = [3,9,20,15,7] and inorder = [9,3,15,20,7], return the binary tree:
```
    3
   / \
  9  20
    /  \
   15   7
```

## Approach
We can solve this problem using recursion by identifying the root node from the preorder array and then finding its position in the inorder array to determine the left and right subtrees. The base case for the recursion is when the array is empty.

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
        
        // The first element of preorder is the root
        TreeNode* root = new TreeNode(preorder[0]);
        
        // Find the index of the root in inorder
        int index = 0;
        while (inorder[index] != preorder[0]) {
            index++;
        }
        
        // Recursively construct the left and right subtrees
        vector<int> leftPreorder(preorder.begin() + 1, preorder.begin() + index + 1);
        vector<int> rightPreorder(preorder.begin() + index + 1, preorder.end());
        vector<int> leftInorder(inorder.begin(), inorder.begin() + index);
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
- The problem can be solved using recursion and array manipulation.
- Identifying the root node from the preorder array and its position in the inorder array is key to solving the problem.
- The base case for the recursion is when the array is empty, at which point we return NULL.