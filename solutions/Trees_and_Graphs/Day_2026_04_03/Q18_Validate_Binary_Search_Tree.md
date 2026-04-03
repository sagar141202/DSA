# Validate Binary Search Tree

## Problem Statement
Given the root of a binary tree, determine if it is a valid binary search tree (BST). A valid BST is defined as a binary tree where for every node, all elements in the left subtree are less than the node, and all elements in the right subtree are greater than the node. The tree must also satisfy the BST property for all nodes. The input tree is represented as a binary tree where each node has a unique value. The function should return true if the tree is a valid BST, and false otherwise. For example, the following tree is a valid BST:       2      / \     1   3. The following tree is not a valid BST:       5      / \     1   4    / \   3   6.

## Approach
The approach to solve this problem is to perform an in-order traversal of the binary tree and check if the resulting sequence is sorted in ascending order. If the sequence is sorted, then the tree is a valid BST. We can also use a recursive approach to check if each subtree is within a valid range.

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
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    bool isValidBST(TreeNode* root) {
        // Initialize the previous node value to negative infinity
        double prev = -1e20;
        
        // Perform an in-order traversal of the tree
        return inOrderTraversal(root, prev);
    }
    
    bool inOrderTraversal(TreeNode* node, double& prev) {
        // Base case: if the node is null, return true
        if (node == nullptr) {
            return true;
        }
        
        // Recursively traverse the left subtree
        if (!inOrderTraversal(node->left, prev)) {
            return false;
        }
        
        // Check if the current node's value is greater than the previous node's value
        if (node->val <= prev) {
            return false;
        }
        
        // Update the previous node's value
        prev = node->val;
        
        // Recursively traverse the right subtree
        return inOrderTraversal(node->right, prev);
    }
};
```

## Test Cases
```
Input: root = [2,1,3]
Output: true
Input: root = [5,1,4,null,null,3,6]
Output: false
```

## Key Takeaways
- We can use an in-order traversal to check if a binary tree is a valid BST.
- The recursive approach allows us to check if each subtree is within a valid range.
- The time complexity of the solution is O(n), where n is the number of nodes in the tree, since we visit each node exactly once.