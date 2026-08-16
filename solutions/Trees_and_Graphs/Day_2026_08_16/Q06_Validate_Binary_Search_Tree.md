# Validate Binary Search Tree

## Problem Statement
Given the root of a binary tree, determine if it is a valid binary search tree (BST). A valid BST is defined as a binary tree where for every node, all elements in the left subtree are less than the node, and all elements in the right subtree are greater than the node. The tree must also satisfy the BST property for all nodes. The input tree is represented as a binary tree where each node has a unique value.

## Approach
The approach is to perform an in-order traversal of the tree and check if the resulting sequence is sorted in ascending order. If the sequence is sorted, then the tree is a valid BST. We can also use a recursive approach to check if each node's value falls within a valid range.

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
    bool isValidBST(TreeNode* root) {
        // Initialize the previous node value to negative infinity
        long long prev = LLONG_MIN;
        
        // Perform in-order traversal
        return inOrderTraversal(root, prev);
    }
    
    bool inOrderTraversal(TreeNode* node, long long& prev) {
        if (!node) return true;
        
        // Traverse the left subtree
        if (!inOrderTraversal(node->left, prev)) return false;
        
        // Check if the current node's value is greater than the previous node's value
        if (node->val <= prev) return false;
        
        // Update the previous node value
        prev = node->val;
        
        // Traverse the right subtree
        return inOrderTraversal(node->right, prev);
    }
};
```

## Test Cases
```
Input: 
     2
    / \
   1   3
Output: true

Input: 
     5
    / \
   1   4
      / \
     3   6
Output: false
```

## Key Takeaways
- A valid BST must satisfy the property that all elements in the left subtree of a node are less than the node, and all elements in the right subtree are greater than the node.
- In-order traversal of a BST results in a sorted sequence.
- Recursive approach can be used to check if each node's value falls within a valid range.