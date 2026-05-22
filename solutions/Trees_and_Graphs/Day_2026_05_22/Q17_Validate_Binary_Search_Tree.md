# Validate Binary Search Tree

## Problem Statement
Given the root of a binary tree, determine if it is a valid binary search tree (BST). A valid BST is a tree where for every node, all elements in the left subtree are less than the node, and all elements in the right subtree are greater than the node. The tree must also satisfy the property that for any node, all elements in the left subtree and right subtree must also follow the same property. The input tree is represented as a binary tree where each node has a unique value. The function should return true if the tree is a valid BST and false otherwise. For example, the tree with the following structure: 
       2
      / \
     1   3
is a valid BST, but the tree with the following structure:
       5
      / \
     1   4
        / \
       3   6
is not a valid BST.

## Approach
We can solve this problem using a recursive or iterative approach, checking each node's value against a valid range. The key idea is to ensure that all nodes in the left subtree have values less than the current node, and all nodes in the right subtree have values greater than the current node. This can be achieved by maintaining a valid range for each node.

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
        return isValidBST(root, LONG_MIN, LONG_MAX);
    }
    
    bool isValidBST(TreeNode* node, long minVal, long maxVal) {
        if (node == NULL) return true;
        
        if (node->val <= minVal || node->val >= maxVal) return false;
        
        return isValidBST(node->left, minVal, node->val) && 
               isValidBST(node->right, node->val, maxVal);
    }
};
```

## Test Cases
```
Input: 
       2
      / \
     1   3
Output: true

Input: 
       5
      / \
     1   4
        / \
       3   6
Output: false
```

## Key Takeaways
- The key to solving this problem is to maintain a valid range for each node.
- The recursive approach is more intuitive and easier to implement.
- The time complexity is O(n) where n is the number of nodes in the tree, and the space complexity is O(h) where h is the height of the tree.