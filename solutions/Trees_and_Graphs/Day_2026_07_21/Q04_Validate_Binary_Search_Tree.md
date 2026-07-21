# Validate Binary Search Tree

## Problem Statement
Given the root of a binary tree, determine if it is a valid binary search tree (BST). A valid BST is defined as a binary tree where for every node, all elements in the left subtree are less than the node, and all elements in the right subtree are greater than the node. The tree must also satisfy the BST property for all nodes. The input tree is represented as a binary tree where each node has a unique integer value. The function should return true if the binary tree is a valid BST, and false otherwise. For example, the binary tree with the following structure: 
       2
      / \
     1   3
is a valid BST, but the binary tree with the following structure:
       5
      / \
     1   4
        / \
       3   6
is not a valid BST.

## Approach
The algorithm will use a recursive in-order traversal to validate the BST property. It checks if the current node's value is within a valid range defined by the minimum and maximum values of its ancestors. If the value is within the range, it recursively checks the left and right subtrees with updated ranges.

## Complexity
- Time: O(N)
- Space: O(H)

## C++ Solution
```cpp
#include <climits>
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
        
        if (root->val <= minVal || root->val >= maxVal) return false;
        
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
Output: True

Input: 
       5
      / \
     1   4
        / \
       3   6
Output: False
```

## Key Takeaways
- The in-order traversal of a valid BST will result in a sorted sequence of node values.
- The recursive approach allows for efficient checking of the BST property for all nodes.
- Using LONG_MIN and LONG_MAX as the initial valid range ensures that all possible integer values can be accommodated.