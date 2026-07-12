# Flatten Binary Tree to Linked List

## Problem Statement
Given the root of a binary tree, flatten the tree into a linked list in-place. The linked list should be in the same order as a pre-order traversal of the tree. The tree nodes should be connected by their right pointers, and the left pointers should be set to NULL. For example, given the following tree:
        1
       / \
      2   5
     / \   \
    3   4   6
The flattened tree should will be:
1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
All nodes should be connected by their right pointers.

## Approach
To solve this problem, we can use a recursive approach where we first flatten the left and right subtrees, then connect the right subtree to the right of the left subtree. We will use a helper function to perform the flattening.

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
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    void flatten(TreeNode* root) {
        // Helper function to flatten the tree
        flattenHelper(root);
    }
    
    // Helper function to flatten the tree
    TreeNode* flattenHelper(TreeNode* node) {
        if (!node) return nullptr;
        
        // Recursively flatten the left and right subtrees
        TreeNode* leftTail = flattenHelper(node->left);
        TreeNode* rightTail = flattenHelper(node->right);
        
        // If the left subtree is not empty, connect it to the right of the node
        if (leftTail) {
            leftTail->right = node->right;
            node->right = node->left;
            node->left = nullptr;
        }
        
        // Return the tail of the flattened subtree
        return rightTail ? rightTail : leftTail ? leftTail : node;
    }
};
```

## Test Cases
```
Input: 
        1
       / \
      2   5
     / \   \
    3   4   6
Output: 
1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
```

## Key Takeaways
- The key to this problem is to use a recursive helper function to flatten the left and right subtrees.
- After flattening the subtrees, we need to connect the right subtree to the right of the left subtree.
- We should also set the left pointer of each node to NULL to ensure the tree is flattened into a linked list.