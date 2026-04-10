# Construct Binary Tree from Preorder and Inorder Traversal

## Problem Statement
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree. The length of both arrays is equal to the number of nodes in the tree. It is guaranteed that the input arrays represent a valid binary tree. For example, given preorder = [3,9,20,15,7] and inorder = [9,3,15,20,7], the output should be a binary tree where 3 is the root, 9 is the left child of 3, and 20 is the right child of 3, with 15 and 7 as the left and right children of 20 respectively.

## Approach
The approach to solve this problem is to use recursion to construct the binary tree. We can identify the root of the tree from the preorder array and then find its position in the inorder array to determine the left and right subtrees. We will use a recursive function to construct the left and right subtrees.

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
        
        // Create a map to store the indices of elements in the inorder array
        unordered_map<int, int> indexMap;
        for (int i = 0; i < inorder.size(); i++) {
            indexMap[inorder[i]] = i;
        }
        
        return buildTreeHelper(preorder, inorder, 0, preorder.size() - 1, 0, inorder.size() - 1, indexMap);
    }
    
    TreeNode* buildTreeHelper(vector<int>& preorder, vector<int>& inorder, int preStart, int preEnd, int inStart, int inEnd, unordered_map<int, int>& indexMap) {
        if (preStart > preEnd || inStart > inEnd) {
            return NULL;
        }
        
        // Create a new node with the current preorder element as the value
        TreeNode* node = new TreeNode(preorder[preStart]);
        
        // Find the index of the current node in the inorder array
        int index = indexMap[node->val];
        
        // Calculate the number of elements in the left subtree
        int leftSize = index - inStart;
        
        // Recursively construct the left and right subtrees
        node->left = buildTreeHelper(preorder, inorder, preStart + 1, preStart + leftSize, inStart, index - 1, indexMap);
        node->right = buildTreeHelper(preorder, inorder, preStart + leftSize + 1, preEnd, index + 1, inEnd, indexMap);
        
        return node;
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
- The key to solving this problem is to identify the root of the tree from the preorder array and then find its position in the inorder array to determine the left and right subtrees.
- Using a recursive function to construct the left and right subtrees simplifies the solution.
- Creating a map to store the indices of elements in the inorder array allows for efficient lookup of the index of the current node.