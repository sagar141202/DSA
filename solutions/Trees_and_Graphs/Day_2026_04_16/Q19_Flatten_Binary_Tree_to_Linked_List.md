# Flatten Binary Tree to Linked List

## Problem Statement
Given the root of a binary tree, flatten the tree into a linked list in-place. The linked list should be made by setting the right child of each node to be its next node in the sequence. The left child of each node should be set to null. For example, given the following tree:
        1
       / \
      2   5
     / \   \
    3   4   6
The flattened tree should look like:
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
We can solve this problem by using a recursive approach, where we first flatten the left and right subtrees, then connect the rightmost node of the left subtree to the root of the right subtree. This way, we can ensure that the tree is flattened in-place.

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
        // Base case: if the tree is empty, return
        if (!root) return;

        // Recursively flatten the left and right subtrees
        flatten(root->left);
        flatten(root->right);

        // If the left subtree is not empty, connect the rightmost node to the right subtree
        if (root->left) {
            // Find the rightmost node in the left subtree
            TreeNode* rightmost = root->left;
            while (rightmost->right) rightmost = rightmost->right;

            // Connect the rightmost node to the right subtree
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
- We use a recursive approach to flatten the left and right subtrees.
- We connect the rightmost node of the left subtree to the root of the right subtree.
- We set the left child of each node to null to ensure that the tree is flattened into a linked list.