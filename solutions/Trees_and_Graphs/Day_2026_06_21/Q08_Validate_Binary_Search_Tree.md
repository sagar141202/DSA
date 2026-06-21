# Validate Binary Search Tree

## Problem Statement
Given the root of a binary tree, determine if it is a valid binary search tree (BST). A valid BST is defined as a binary tree where for every node, all elements in its left subtree are less than the node, and all elements in its right subtree are greater than the node. The tree must also satisfy the property that for any node, all elements in the left subtree and right subtree must also follow the same property. The input tree is represented as a binary tree where each node has a unique value. The function should return true if the tree is a valid BST, and false otherwise. For example, the tree with root [2,1,3] is a valid BST, but the tree with root [5,1,4,null,null,3,6] is not.

## Approach
We will use a recursive approach to traverse the tree and validate if each node's value falls within a valid range. The range will be updated as we traverse down the tree to ensure the BST property is maintained. We will check if the current node's value is within the valid range and then update the range for the left and right child nodes.

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
Input: root = [2,1,3]
Output: true
Input: root = [5,1,4,null,null,3,6]
Output: false
```

## Key Takeaways
- Recursive approach is suitable for tree traversal problems.
- Using a valid range to track the allowed values for each node helps in validating the BST property.
- The time complexity is O(n) where n is the number of nodes in the tree, as we visit each node once.