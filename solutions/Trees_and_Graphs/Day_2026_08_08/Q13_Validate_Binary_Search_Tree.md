# Validate Binary Search Tree

## Problem Statement
Given the root of a binary tree, determine if it is a valid binary search tree (BST). A valid BST is defined as a binary tree where for every node, all elements in the left subtree are less than the node, and all elements in the right subtree are greater than the node. The tree must also satisfy the property that for any node, all elements in the left subtree and right subtree must also follow the same property. The input tree is represented as a binary tree where each node has a unique value. The tree has at most 100 nodes, and each node has a value between -2^31 and 2^31 - 1.

## Approach
The approach to solve this problem is to use a recursive function that checks if each node's value falls within a valid range. We start by assigning a valid range to the root node and then recursively check the left and right child nodes with updated valid ranges.

## Complexity
- Time: O(N)
- Space: O(N)

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
        return isValidBSTHelper(root, LONG_MIN, LONG_MAX);
    }
    
    bool isValidBSTHelper(TreeNode* node, long minVal, long maxVal) {
        // Base case: an empty tree is a valid BST
        if (node == NULL) return true;
        
        // If the current node's value is not within the valid range, return false
        if (node->val <= minVal || node->val >= maxVal) return false;
        
        // Recursively check the left and right subtrees with updated valid ranges
        return isValidBSTHelper(node->left, minVal, node->val) && 
               isValidBSTHelper(node->right, node->val, maxVal);
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
- Use a recursive approach to check the validity of each node in the binary tree.
- Assign a valid range to each node and update the range for the left and right child nodes.
- Use a helper function to simplify the recursive approach and avoid redundant code.