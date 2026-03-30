# Validate Binary Search Tree

## Problem Statement
Given the root of a binary tree, determine if it is a valid binary search tree (BST). A valid BST is defined as a binary tree where for every node, all elements in the left subtree are less than the node, and all elements in the right subtree are greater than the node. The problem requires checking if the given binary tree satisfies this property for all nodes. The tree has at most 10^4 nodes and each node has a unique value between -2^31 and 2^31 - 1.

## Approach
The approach involves performing an in-order traversal of the binary tree and checking if the resulting sequence is strictly increasing. This is because an in-order traversal of a BST visits nodes in ascending order. If the sequence is strictly increasing, the binary tree is a valid BST.

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
        // Initialize the previous node value
        long long prev = LLONG_MIN;
        
        // Perform in-order traversal
        return inOrderTraversal(root, prev);
    }
    
    bool inOrderTraversal(TreeNode* node, long long& prev) {
        // Base case: empty tree
        if (node == nullptr) {
            return true;
        }
        
        // Traverse the left subtree
        if (!inOrderTraversal(node->left, prev)) {
            return false;
        }
        
        // Check if the current node value is greater than the previous node value
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
Input: root = [2,1,3]
Output: true

Input: root = [5,1,4,null,null,3,6]
Output: false
```

## Key Takeaways
- A valid BST must have all elements in the left subtree less than the node, and all elements in the right subtree greater than the node.
- In-order traversal of a BST visits nodes in ascending order, which can be used to validate the BST property.
- The time complexity of this solution is O(n), where n is the number of nodes in the tree, since we visit each node once during the in-order traversal.