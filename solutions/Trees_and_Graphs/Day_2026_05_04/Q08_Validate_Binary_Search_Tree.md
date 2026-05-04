# Validate Binary Search Tree

## Problem Statement
Given the root of a binary tree, determine if it is a valid binary search tree (BST). A valid BST is defined as a binary tree where for every node, all elements in the left subtree are less than the node, and all elements in the right subtree are greater than the node. The tree must also satisfy the BST property for all nodes. The input tree is represented as a binary tree where each node has a unique value. Constraints: 1 <= number of nodes <= 10^4, -2^31 <= node values <= 2^31 - 1.

## Approach
We can solve this problem by performing an in-order traversal of the tree and checking if the resulting sequence is sorted in ascending order. If it is, then the tree is a valid BST. We can use a recursive or iterative approach to perform the in-order traversal.

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
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    bool isValidBST(TreeNode* root) {
        // Initialize the previous node value to negative infinity
        long long prev = LLONG_MIN;
        
        // Perform in-order traversal and check if the resulting sequence is sorted
        return inOrderTraversal(root, prev);
    }
    
    bool inOrderTraversal(TreeNode* node, long long& prev) {
        if (node == nullptr) return true;
        
        // Recursively traverse the left subtree
        if (!inOrderTraversal(node->left, prev)) return false;
        
        // Check if the current node value is greater than the previous node value
        if (node->val <= prev) return false;
        
        // Update the previous node value
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
- A valid BST must satisfy the property that all elements in the left subtree are less than the node, and all elements in the right subtree are greater than the node.
- In-order traversal can be used to check if a binary tree is a valid BST by verifying that the resulting sequence is sorted in ascending order.
- Recursive or iterative approaches can be used to perform the in-order traversal.