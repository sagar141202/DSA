# Validate Binary Search Tree

## Problem Statement
Given the root of a binary tree, determine if it is a valid binary search tree (BST). A valid BST is defined as a binary tree where for every node, all elements in the left subtree are less than the node, and all elements in the right subtree are greater than the node. The tree must also satisfy the BST property for all nodes. For example, the following tree is a valid BST:
       2
      / \
     1   3
However, the following tree is not a valid BST:
       5
      / \
     1   4
        / \
       3   6
The input will be the root of the binary tree, and the output should be a boolean indicating whether the tree is a valid BST.

## Approach
We can solve this problem by performing an in-order traversal of the tree and checking if the resulting sequence is sorted in ascending order. This works because in a valid BST, an in-order traversal will always produce a sorted sequence.

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
    
    bool inOrderTraversal(TreeNode* node, long long& prev) {
        // Base case: if the node is null, return true
        if (node == nullptr) {
            return true;
        }
        
        // Recursively traverse the left subtree
        if (!inOrderTraversal(node->left, prev)) {
            return false;
        }
        
        // Check if the current node value is greater than the previous node value
        if (node->val <= prev) {
            return false;
        }
        
        // Update the previous node value
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
- A valid BST must satisfy the BST property for all nodes.
- In-order traversal of a valid BST produces a sorted sequence in ascending order.
- We can use recursion to perform the in-order traversal and check the BST property.