# Validate Binary Search Tree

## Problem Statement
Given the root of a binary tree, determine if it is a valid binary search tree (BST). A valid BST is defined as a binary tree where for every node, all elements in the left subtree are less than the node, and all elements in the right subtree are greater than the node. The left and right subtrees must also be valid BSTs. The input tree is represented as a binary tree where each node has a unique value. Constraints: The number of nodes in the tree is in the range [1, 104]. The values of the nodes in the tree are in the range [231, 231 - 1]. Examples: Input: root = [2,1,3], Output: true; Input: root = [5,1,4,null,null,3,6], Output: false.

## Approach
We will use a recursive approach to validate the BST, checking if each node's value falls within a valid range. The range will be updated as we traverse the tree. This approach ensures that all nodes satisfy the BST property.

## Complexity
- Time: O(N)
- Space: O(H)

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
        return validate(node->left, minVal, node->val) && validate(node->right, node->val, maxVal);
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
- Use recursive approach to simplify the validation process.
- Update the valid range as we traverse the tree to ensure BST property.
- Handle edge cases where the tree is empty or contains a single node.