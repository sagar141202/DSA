# Validate Binary Search Tree

## Problem Statement
Given the root of a binary tree, determine if it is a valid binary search tree. A valid binary search tree is defined as a binary tree where for every node, all elements in its left subtree are less than the node, and all elements in its right subtree are greater than the node. The left and right subtrees must also be binary search trees. The input tree is non-empty and has at most 100 nodes.

## Approach
The approach is to perform an in-order traversal of the binary tree and check if the resulting sequence is strictly increasing. If it is, then the binary tree is a valid binary search tree. We can also use a recursive approach to check if each subtree is within a valid range.

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
        // Initialize the previous node value
        long long prev = LLONG_MIN;
        
        // Perform in-order traversal
        return inOrderTraversal(root, prev);
    }
    
    bool inOrderTraversal(TreeNode* root, long long& prev) {
        // Base case: if the tree is empty, it is a valid BST
        if (root == nullptr) {
            return true;
        }
        
        // Traverse the left subtree
        if (!inOrderTraversal(root->left, prev)) {
            return false;
        }
        
        // Check if the current node's value is greater than the previous node's value
        if (root->val <= prev) {
            return false;
        }
        
        // Update the previous node's value
        prev = root->val;
        
        // Traverse the right subtree
        return inOrderTraversal(root->right, prev);
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
- A valid binary search tree must satisfy the property that all elements in the left subtree of a node are less than the node, and all elements in the right subtree are greater than the node.
- In-order traversal of a binary search tree results in a strictly increasing sequence.
- Recursive approach can be used to check if each subtree is within a valid range.