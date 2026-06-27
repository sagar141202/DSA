# Flatten Binary Tree to Linked List

## Problem Statement
Given the root of a binary tree, flatten the tree into a linked list in-place. The linked list should be made by using the right child pointer of each node to point to the next node in the sequence. The left child of each node should be set to nullptr. For example, given the following tree:
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
You are not allowed to use any extra space.

## Approach
The approach is to use a recursive function to traverse the tree and flatten it in-place. We will use a previous pointer to keep track of the previous node in the sequence. We will then use this pointer to update the right child of each node.

## Complexity
- Time: O(n)
- Space: O(n)

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
        if (!root) return;
        flattenHelper(root);
    }
    
    // Helper function to flatten the tree
    TreeNode* flattenHelper(TreeNode* node) {
        if (!node) return nullptr;
        
        // Recursively flatten the left and right subtrees
        TreeNode* leftTail = flattenHelper(node->left);
        TreeNode* rightTail = flattenHelper(node->right);
        
        // If the left subtree is not empty, update the right child of the left tail
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
Input: [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]
```

## Key Takeaways
- We need to use a recursive function to traverse the tree and flatten it in-place.
- We use a previous pointer to keep track of the previous node in the sequence.
- We update the right child of each node using the previous pointer.