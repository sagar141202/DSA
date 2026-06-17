# Flatten Binary Tree to Linked List

## Problem Statement
Given the root of a binary tree, flatten the tree into a linked list in-place. The linked list should be made by using the right child pointer and each right child should point to the next node in the sequence. The left child of each node should be set to nullptr. For example, given the following tree:
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

## Approach
To solve this problem, we will use a recursive approach to traverse the tree and flatten it. We will use a helper function to perform the flattening. The function will take a node and return the last node in the flattened subtree.

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
        flattenHelper(root);
    }
    
    // Helper function to perform the flattening
    TreeNode* flattenHelper(TreeNode* node) {
        if (node == nullptr) return nullptr;
        
        // Recursively flatten the left and right subtrees
        TreeNode* leftTail = flattenHelper(node->left);
        TreeNode* rightTail = flattenHelper(node->right);
        
        // If the left subtree is not empty, append it to the right subtree
        if (leftTail != nullptr) {
            leftTail->right = node->right;
            node->right = node->left;
            node->left = nullptr;
        }
        
        // Return the last node in the flattened subtree
        return rightTail == nullptr ? leftTail : rightTail;
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
- Recursively traverse the tree and flatten each subtree.
- Use a helper function to perform the flattening and return the last node in the flattened subtree.
- Update the child pointers of each node to form the linked list.