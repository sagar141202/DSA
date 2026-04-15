# Validate Binary Search Tree

## Problem Statement
Given the root of a binary tree, determine if it is a valid binary search tree (BST). A valid BST is defined as a binary tree where for every node, all elements in the left subtree are less than the node, and all elements in the right subtree are greater than the node. The left and right subtrees must also be valid BSTs. For example, the binary tree with root [2,1,3] is a valid BST, but the binary tree with root [5,1,4,null,null,3,6] is not.

## Approach
We can solve this problem by performing an in-order traversal of the tree and checking if the resulting sequence is sorted in ascending order. If the sequence is sorted, then the tree is a valid BST. We can also use a recursive approach to check if each subtree is a valid BST.

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
        // Base case: if the node is null, return true
        if (node == NULL) return true;
        
        // Traverse the left subtree
        if (!inOrderTraversal(node->left, prev)) return false;
        
        // Check if the current node value is greater than the previous node value
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
Input: [2,1,3]
Output: true
Input: [5,1,4,null,null,3,6]
Output: false
```

## Key Takeaways
- A valid BST is defined as a binary tree where for every node, all elements in the left subtree are less than the node, and all elements in the right subtree are greater than the node.
- We can solve this problem by performing an in-order traversal of the tree and checking if the resulting sequence is sorted in ascending order.
- The time complexity of the solution is O(n), where n is the number of nodes in the tree, and the space complexity is O(h), where h is the height of the tree.