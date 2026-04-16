# Validate Binary Search Tree

## Problem Statement
Given the root of a binary tree, determine if it is a valid binary search tree (BST). A valid BST is defined as a binary tree where for every node, all elements in the left subtree are less than the node, and all elements in the right subtree are greater than the node. The input tree will have at most 100 nodes, and each node will have a unique value between -2^31 and 2^31 - 1.

## Approach
We can solve this problem by performing an in-order traversal of the tree and checking if the resulting sequence is sorted in ascending order. If it is, then the tree is a valid BST. We can also use a recursive approach with a valid range for each node.

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
        
        // Perform in-order traversal
        return inOrderTraversal(root, prev);
    }
    
    bool inOrderTraversal(TreeNode* node, long long& prev) {
        // Base case: empty tree
        if (node == NULL) {
            return true;
        }
        
        // Traverse the left subtree
        if (!inOrderTraversal(node->left, prev)) {
            return false;
        }
        
        // Check if the current node value is valid
        if (node->val <= prev) {
            return false;
        }
        
        // Update the previous node value
        prev = node->val;
        
        // Traverse the right subtree
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
- Use in-order traversal to check if a binary tree is a valid BST.
- Keep track of the previous node value to check for validity.
- Use a recursive approach with a valid range for each node as an alternative solution.