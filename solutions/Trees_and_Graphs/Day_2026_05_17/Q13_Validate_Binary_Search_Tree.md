# Validate Binary Search Tree

## Problem Statement
Given the root of a binary tree, determine if it is a valid binary search tree. A valid binary search tree is defined as a binary tree in which the left subtree of a node contains only nodes with values less than the node's value, the right subtree of a node contains only nodes with values greater than the node's value, and both the left and right subtrees must also be binary search trees. The tree has at most 10^4 nodes and each node's value is between -2^31 and 2^31 - 1.

## Approach
We can solve this problem by performing an in-order traversal of the tree and checking if the values are in ascending order. If they are, then the tree is a valid binary search tree. This approach works because in a binary search tree, an in-order traversal will always produce a sorted sequence of values.

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
        // Initialize the previous value to negative infinity
        long long prev = LLONG_MIN;
        
        // Perform an in-order traversal of the tree
        return inOrderTraversal(root, prev);
    }
    
    bool inOrderTraversal(TreeNode* node, long long& prev) {
        // Base case: if the node is null, return true
        if (node == NULL) return true;
        
        // Recursively traverse the left subtree
        if (!inOrderTraversal(node->left, prev)) return false;
        
        // Check if the current node's value is greater than the previous value
        if (node->val <= prev) return false;
        
        // Update the previous value
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
- A binary search tree must satisfy the property that all elements in the left subtree are less than the root, and all elements in the right subtree are greater than the root.
- An in-order traversal of a binary search tree will always produce a sorted sequence of values.
- This solution uses a recursive approach to perform the in-order traversal and check the validity of the binary search tree.