# Validate Binary Search Tree

## Problem Statement
Given the root of a binary tree, determine if it is a valid binary search tree (BST). A valid BST is defined as a binary tree where for every node, all elements in the left subtree are less than the node, and all elements in the right subtree are greater than the node. The tree must also satisfy the BST property for all nodes. For example, the tree with root [2,1,3] is a valid BST, but the tree with root [5,1,4,null,null,3,6] is not.

## Approach
We can validate a binary search tree by performing an in-order traversal and checking if the elements are in ascending order. If they are, then the tree is a valid BST. We can also use a recursive approach with a valid range for each node.

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
        long long prev = LLONG_MIN;
        
        // Perform in-order traversal
        return inOrderTraversal(root, prev);
    }
    
    bool inOrderTraversal(TreeNode* node, long long& prev) {
        // Base case: if the node is null, return true
        if (node == nullptr) return true;
        
        // Recursively traverse the left subtree
        if (!inOrderTraversal(node->left, prev)) return false;
        
        // Check if the current node's value is greater than the previous node's value
        if (node->val <= prev) return false;
        
        // Update the previous node's value
        prev = node->val;
        
        // Recursively traverse the right subtree
        return inOrderTraversal(node->right, prev);
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
- A binary search tree can be validated using an in-order traversal.
- The in-order traversal visits nodes in ascending order for a valid BST.
- Recursive and iterative approaches can be used to validate a BST.