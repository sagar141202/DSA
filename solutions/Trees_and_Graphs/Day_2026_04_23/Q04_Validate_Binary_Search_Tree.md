# Validate Binary Search Tree

## Problem Statement
Given the root of a binary tree, determine if it is a valid binary search tree (BST). A valid BST is defined as a binary tree where for every node, all elements in the left subtree are less than the node, and all elements in the right subtree are greater than the node. The left and right subtrees must also be valid BSTs. The input tree is guaranteed to have at most 2^31 - 1 nodes and the values of the nodes are in the range [Integer.MIN_VALUE, Integer.MAX_VALUE]. For example, the following tree is a valid BST: 
       2
      / \
     1   3
But the following tree is not:
       5
      / \
     1   4
        / \
       3   6

## Approach
To validate a binary search tree, we can use a recursive approach with a helper function that checks if a subtree is within a valid range. We start by checking the root node and then recursively check the left and right subtrees.

## Complexity
- Time: O(N)
- Space: O(H)

## C++ Solution
```cpp
#include <climits>
using namespace std;
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
        if (node == NULL) return true;
        
        if (node->val <= minVal || node->val >= maxVal) return false;
        
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
- We use a recursive helper function to check the validity of the BST.
- The helper function checks if the current node's value is within a valid range.
- The valid range is updated for the left and right subtrees.