# Validate Binary Search Tree

## Problem Statement
Given the root of a binary tree, determine if it is a valid binary search tree (BST). A valid BST is defined as a binary tree where for every node, all elements in the left subtree are less than the node, and all elements in the right subtree are greater than the node. The tree must also satisfy the property that for any node, all elements in the left subtree and right subtree must also follow the same property. The input tree is represented as a binary tree where each node has a unique integer value.

## Approach
The algorithm checks each node in the tree to ensure it satisfies the BST property by maintaining a valid range for each node. The root node has an initial valid range from negative infinity to positive infinity. For each node, we update the valid range based on whether it's a left or right child and check if the node's value falls within this range.

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
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    bool isValidBST(TreeNode* root) {
        return isValidBST(root, LONG_MIN, LONG_MAX);
    }
    
    bool isValidBST(TreeNode* root, long minVal, long maxVal) {
        if (root == NULL) return true;
        
        // Check if current node's value is within valid range
        if (root->val <= minVal || root->val >= maxVal) return false;
        
        // Recursively check left and right subtrees with updated valid ranges
        return isValidBST(root->left, minVal, root->val) && 
               isValidBST(root->right, root->val, maxVal);
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
- A valid BST must satisfy the property that for any node, all elements in the left subtree are less than the node, and all elements in the right subtree are greater than the node.
- The algorithm uses a recursive approach to check each node in the tree against a valid range.
- The time complexity is O(N), where N is the number of nodes in the tree, and the space complexity is O(H), where H is the height of the tree.