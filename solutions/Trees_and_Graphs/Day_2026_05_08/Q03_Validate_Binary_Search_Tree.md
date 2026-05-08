# Validate Binary Search Tree

## Problem Statement
Given the root of a binary tree, determine if it is a valid binary search tree (BST). A valid BST is defined as a binary tree where for every node, all elements in the left subtree are less than the node, and all elements in the right subtree are greater than the node. The left and right subtrees must also be valid BSTs. The tree has at most 10^4 nodes and each node has a unique value between -2^31 and 2^31 - 1.

## Approach
We can solve this problem using a recursive approach by checking if each node's value falls within a valid range. We will define the valid range for each node based on its parent nodes. The algorithm will return false as soon as it finds a node that does not satisfy the BST property.

## Complexity
- Time: O(n)
- Space: O(h), where h is the height of the tree

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
        return validate(root, LONG_MIN, LONG_MAX);
    }

    bool validate(TreeNode* node, long minVal, long maxVal) {
        if (!node) return true;

        if (node->val <= minVal || node->val >= maxVal) return false;

        return validate(node->left, minVal, node->val) && 
               validate(node->right, node->val, maxVal);
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
- Use a recursive approach to check the validity of the BST.
- Define the valid range for each node based on its parent nodes.
- Use LONG_MIN and LONG_MAX as the initial valid range for the root node.