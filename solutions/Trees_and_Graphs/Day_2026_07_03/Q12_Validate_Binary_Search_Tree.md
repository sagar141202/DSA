# Validate Binary Search Tree

## Problem Statement
Given the root of a binary tree, determine if it is a valid binary search tree (BST). A valid BST is defined as a binary tree where for every node, all elements in the left subtree are less than the node, and all elements in the right subtree are greater than the node. The tree must also satisfy the BST property for all nodes. The input tree is represented as a binary tree where each node has a unique value. The function should return true if the tree is a valid BST, and false otherwise. For example, the tree with root node having value 2, left child having value 1, and right child having value 3 is a valid BST, but the tree with root node having value 1, left child having value 2, and right child having value 3 is not.

## Approach
The algorithm checks each node in the tree to ensure it satisfies the BST property by recursively verifying the left and right subtrees. It uses a recursive approach with a helper function to validate the tree, passing the valid range for each node. The function returns false as soon as it finds a node that does not satisfy the BST property.

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
        return validate(root, LONG_MIN, LONG_MAX);
    }
    
    bool validate(TreeNode* node, long minVal, long maxVal) {
        if (node == NULL) return true;
        
        if (node->val <= minVal || node->val >= maxVal) {
            return false;
        }
        
        return validate(node->left, minVal, node->val) && 
               validate(node->right, node->val, maxVal);
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
- The key insight is to use a recursive approach to validate each node in the tree while maintaining a valid range for each node's value.
- We use LONG_MIN and LONG_MAX to represent negative and positive infinity, ensuring all node values fall within the valid range.
- The time complexity is O(n) because we visit each node exactly once, and the space complexity is O(h) due to the recursive call stack, where h is the height of the tree.