# Validate Binary Search Tree

## Problem Statement
Given the root of a binary tree, determine if it is a valid binary search tree (BST). A valid BST is defined as a binary tree where for every node, all elements in the left subtree are less than the node, and all elements in the right subtree are greater than the node. The tree must also satisfy the BST property for all nodes. The input tree is represented as a binary tree where each node has a unique value. The function should return true if the tree is a valid BST, and false otherwise. For example, the binary tree [2,1,3] is a valid BST, but the binary tree [5,1,4,null,null,3,6] is not.

## Approach
The algorithm uses a recursive approach to check if each node's value falls within a valid range. The range is updated as we traverse the tree, ensuring that all nodes satisfy the BST property. We use a helper function to perform the recursive checks. The function checks if the current node's value is within the valid range and then recursively checks the left and right subtrees.

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
        return helper(root, LONG_MIN, LONG_MAX);
    }
    
    bool helper(TreeNode* node, long minVal, long maxVal) {
        // base case: empty tree
        if (node == nullptr) {
            return true;
        }
        
        // check if current node's value is within the valid range
        if (node->val <= minVal || node->val >= maxVal) {
            return false;
        }
        
        // recursively check left and right subtrees with updated ranges
        return helper(node->left, minVal, node->val) && helper(node->right, node->val, maxVal);
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
- A valid BST requires all nodes to satisfy the BST property.
- Recursive approaches can be used to check the validity of a BST.
- Updating the valid range as we traverse the tree ensures that all nodes satisfy the BST property.