# Validate Binary Search Tree

## Problem Statement
Given the root of a binary tree, determine if it is a valid binary search tree (BST). A valid BST is defined as a binary tree where for every node, all elements in the left subtree are less than the node, and all elements in the right subtree are greater than the node. The tree must also satisfy the BST property for all nodes. The input tree is represented as a binary tree where each node has a unique integer value. The function should return true if the binary tree is a valid BST, and false otherwise. For example, the binary tree represented by the following nodes: 2, 1, 3 is a valid BST, but the binary tree represented by the following nodes: 5, 1, 4, null, null, 3, 6 is not a valid BST.

## Approach
The approach is to perform an in-order traversal of the binary tree and store the node values in a vector. Then, check if the vector is sorted in ascending order. If it is, the binary tree is a valid BST. This solution works because in-order traversal of a BST always produces a sorted sequence.

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
        // Initialize a vector to store the in-order traversal of the tree
        vector<int> inOrder;
        
        // Perform in-order traversal and store the node values in the vector
        inOrderTraversal(root, inOrder);
        
        // Check if the vector is sorted in ascending order
        for (int i = 0; i < inOrder.size() - 1; i++) {
            if (inOrder[i] >= inOrder[i + 1]) {
                return false;
            }
        }
        
        return true;
    }
    
    // Helper function to perform in-order traversal
    void inOrderTraversal(TreeNode* node, vector<int>& inOrder) {
        if (node == nullptr) {
            return;
        }
        
        inOrderTraversal(node->left, inOrder);
        inOrder.push_back(node->val);
        inOrderTraversal(node->right, inOrder);
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
- A valid BST is a binary tree where for every node, all elements in the left subtree are less than the node, and all elements in the right subtree are greater than the node.
- In-order traversal of a BST always produces a sorted sequence.
- The time complexity of this solution is O(n), where n is the number of nodes in the tree, because we visit each node once during the in-order traversal.