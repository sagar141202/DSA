# Validate Binary Search Tree

## Problem Statement
Given the root of a binary tree, determine if it is a valid binary search tree (BST). A valid BST is defined as a binary tree where for every node, all elements in the left subtree are less than the node, and all elements in the right subtree are greater than the node. The tree must also satisfy the BST property for all nodes. The input tree is represented as a binary tree where each node has a unique value. The function should return true if the tree is a valid BST, and false otherwise. For example, the binary tree [2,1,3] is a valid BST, but the binary tree [5,1,4,null,null,3,6] is not.

## Approach
We will use a recursive approach to validate the binary search tree, checking each node's value against a valid range. The algorithm will ensure that for every node, all elements in the left subtree are less than the node, and all elements in the right subtree are greater than the node.

## Complexity
- Time: O(n)
- Space: O(h)

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
    bool isValidBST(TreeNode* root) {
        return isValidBSTHelper(root, LONG_MIN, LONG_MAX);
    }
    
    bool isValidBSTHelper(TreeNode* node, long minVal, long maxVal) {
        // base case: an empty tree is a valid BST
        if (node == NULL) {
            return true;
        }
        
        // check if the current node's value is within the valid range
        if (node->val <= minVal || node->val >= maxVal) {
            return false;
        }
        
        // recursively check the left and right subtrees
        return isValidBSTHelper(node->left, minVal, node->val) &&
               isValidBSTHelper(node->right, node->val, maxVal);
    }
};
```

## Test Cases
```
Input: [2,1,3]
Output: true

Input: [5,1,4,null,null,3,6]
Output: false
```

## Key Takeaways
- A valid binary search tree must satisfy the BST property for all nodes.
- The recursive approach is suitable for validating a binary search tree.
- The time complexity of the solution is O(n), where n is the number of nodes in the tree.