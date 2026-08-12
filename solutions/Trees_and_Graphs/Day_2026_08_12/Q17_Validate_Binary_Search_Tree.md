# Validate Binary Search Tree

## Problem Statement
Given the root of a binary tree, determine if it is a valid binary search tree (BST). A valid BST is defined as a binary tree where for every node, all elements in the left subtree are less than the node, and all elements in the right subtree are greater than the node. The tree must also satisfy the BST property for all nodes. For example, the tree with root node having value 2, left child having value 1, and right child having value 3 is a valid BST, but the tree with root node having value 1, left child having value 2, and right child having value 3 is not a valid BST.

## Approach
The algorithm checks each node in the tree to ensure it satisfies the BST property. It uses a recursive approach, checking the left and right subtrees of each node. The key insight is to keep track of the valid range for each node, ensuring all values in the left subtree are less than the node and all values in the right subtree are greater.

## Complexity
- Time: O(N)
- Space: O(H), where N is the number of nodes and H is the height of the tree

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
        return isValidBSTHelper(root, LONG_MIN, LONG_MAX);
    }

    bool isValidBSTHelper(TreeNode* node, long minVal, long maxVal) {
        // Base case: an empty tree is a valid BST
        if (node == NULL) {
            return true;
        }

        // Check if the current node's value is within the valid range
        if (node->val <= minVal || node->val >= maxVal) {
            return false;
        }

        // Recursively check the left and right subtrees with updated valid ranges
        return isValidBSTHelper(node->left, minVal, node->val) &&
               isValidBSTHelper(node->right, node->val, maxVal);
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
- Recursive approach can be used to validate a BST by checking each node against a valid range.
- The valid range for each node is updated as we traverse down the tree, ensuring all values in the left subtree are less than the node and all values in the right subtree are greater.
- The time complexity is O(N), where N is the number of nodes in the tree, since we visit each node once.