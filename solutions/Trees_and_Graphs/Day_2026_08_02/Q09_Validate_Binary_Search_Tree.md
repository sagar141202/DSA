# Validate Binary Search Tree

## Problem Statement
Given the root of a binary tree, determine if it is a valid binary search tree (BST). A valid BST is defined as a binary tree where for every node, all elements in the left subtree are less than the node, and all elements in the right subtree are greater than the node. The left and right subtrees must also be valid BSTs. The input tree is represented as a binary tree where each node has a unique value and has at most two children (i.e., left child and right child).

## Approach
To validate a binary search tree, we can perform an in-order traversal and check if the resulting sequence is sorted in ascending order. This approach works because in a valid BST, the in-order traversal visits nodes in ascending order.

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
        
        // Perform in-order traversal
        return inOrderTraversal(root, prev);
    }
    
    bool inOrderTraversal(TreeNode* node, long long& prev) {
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
- A valid binary search tree can be validated using in-order traversal.
- The in-order traversal of a valid BST visits nodes in ascending order.
- The time complexity of this approach is O(n), where n is the number of nodes in the tree.