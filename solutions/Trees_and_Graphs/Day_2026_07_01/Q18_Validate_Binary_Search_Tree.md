# Validate Binary Search Tree

## Problem Statement
Given the root of a binary tree, determine if it is a valid binary search tree (BST). A valid BST is defined as a binary tree where for every node, all elements in the left subtree are less than the node, and all elements in the right subtree are greater than the node. The tree must also satisfy the BST property for all nodes. The input tree is represented as a binary tree where each node has a unique value. The tree has at most 100 nodes and the values of the nodes are in the range [0, 100]. For example, the binary tree with the following structure: 
       2
      / \
     1   3
is a valid BST, but the binary tree with the following structure:
       1
      / \
     2   3
is not a valid BST.

## Approach
The approach to solve this problem is to perform an in-order traversal of the binary tree and check if the traversed nodes are in ascending order. If they are, then the tree is a valid BST. We can use a recursive or iterative approach to perform the in-order traversal. The key idea is to keep track of the previous node's value and compare it with the current node's value.

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
        // Initialize the previous node's value to negative infinity
        long long prev = LLONG_MIN;
        
        // Perform in-order traversal and check if the tree is a valid BST
        return inOrder(root, prev);
    }
    
    bool inOrder(TreeNode* node, long long& prev) {
        // Base case: if the node is null, return true
        if (node == nullptr) return true;
        
        // Recursively traverse the left subtree
        if (!inOrder(node->left, prev)) return false;
        
        // Check if the current node's value is greater than the previous node's value
        if (node->val <= prev) return false;
        
        // Update the previous node's value
        prev = node->val;
        
        // Recursively traverse the right subtree
        return inOrder(node->right, prev);
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
- The key to solving this problem is to use in-order traversal to check if the tree is a valid BST.
- We need to keep track of the previous node's value to compare it with the current node's value.
- The time complexity of the solution is O(n), where n is the number of nodes in the tree, and the space complexity is O(h), where h is the height of the tree.