# Flatten Binary Tree to Linked List

## Problem Statement
Given the root of a binary tree, flatten the tree into a linked list in-place. The linked list should be in the same order as a pre-order traversal of the binary tree. The tree nodes should be connected by their right pointers. For example, given the following tree:
        1
       / \
      2   5
     / \   \
    3   4   6
The flattened tree should be:
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
The algorithm involves a recursive pre-order traversal of the binary tree, where each node's left child is appended to its right child. This process continues until the entire tree is flattened into a linked list.

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
        if (root == nullptr) return;
        
        // Recursively flatten the left and right subtrees
        flatten(root->left);
        flatten(root->right);
        
        // If the left subtree is not empty, append it to the right subtree
        if (root->left != nullptr) {
            // Find the rightmost node in the left subtree
            TreeNode* rightmost = root->left;
            while (rightmost->right != nullptr) {
                rightmost = rightmost->right;
            }
            
            // Append the left subtree to the right subtree
            rightmost->right = root->right;
            root->right = root->left;
            root->left = nullptr;
        }
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
- The key to solving this problem is to recursively flatten the left and right subtrees.
- After flattening the subtrees, we need to append the left subtree to the right subtree if the left subtree is not empty.
- We use a while loop to find the rightmost node in the left subtree and append the right subtree to it.