# Validate Binary Search Tree

## Problem Statement
Given the root of a binary tree, determine if it is a valid binary search tree (BST). A valid BST is defined as a binary tree where for every node, all elements in its left subtree are less than the node, and all elements in its right subtree are greater than the node. The left and right subtrees must also be valid BSTs. The tree has at most 10^4 nodes, and each node's value is between -2^31 and 2^31 - 1.

## Approach
We can solve this problem by performing an in-order traversal of the tree and checking if the resulting sequence is sorted in ascending order. If it is, then the tree is a valid BST. We will use a recursive approach to traverse the tree and check for validity.

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
        // Initialize the previous node value
        long long prev = LLONG_MIN;
        
        // Perform in-order traversal and check for validity
        return inOrderTraversal(root, prev);
    }
    
    bool inOrderTraversal(TreeNode* node, long long& prev) {
        if (node == NULL) return true;
        
        // Traverse the left subtree
        if (!inOrderTraversal(node->left, prev)) return false;
        
        // Check if the current node's value is greater than the previous node's value
        if (node->val <= prev) return false;
        prev = node->val;
        
        // Traverse the right subtree
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
- A valid BST is a binary tree where for every node, all elements in its left subtree are less than the node, and all elements in its right subtree are greater than the node.
- In-order traversal of a valid BST results in a sorted sequence in ascending order.
- We can use a recursive approach to traverse the tree and check for validity.