# Validate Binary Search Tree

## Problem Statement
Given the root of a binary tree, determine if it is a valid binary search tree (BST). A valid BST is defined as a binary tree where for every node, all elements in the left subtree are less than the node, and all elements in the right subtree are greater than the node. The left and right subtrees must also be valid BSTs. The tree has at most 10^4 nodes, and each node has a unique value between -2^31 and 2^31 - 1.

## Approach
We will use a recursive approach to validate the BST, checking each node's value against a valid range. The algorithm will traverse the tree, updating the valid range for each node based on its position in the tree. If any node's value falls outside its valid range, the tree is not a valid BST.

## Complexity
- Time: O(N)
- Space: O(H), where N is the number of nodes and H is the height of the tree

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
        
        // Check if node's value is within valid range
        if (node->val <= minVal || node->val >= maxVal) return false;
        
        // Recursively check left and right subtrees with updated ranges
        return isValidBST(node->left, minVal, node->val) && 
               isValidBST(node->right, node->val, maxVal);
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
- Use a recursive approach to validate the BST, checking each node's value against a valid range.
- Update the valid range for each node based on its position in the tree.
- If any node's value falls outside its valid range, the tree is not a valid BST.