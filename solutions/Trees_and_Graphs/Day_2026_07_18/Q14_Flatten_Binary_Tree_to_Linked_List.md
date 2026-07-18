# Flatten Binary Tree to Linked List

## Problem Statement
Given the root of a binary tree, flatten the tree into a linked list in-place. The linked list should be formed by concatenating the left and right child nodes in the order they appear in a pre-order traversal of the tree. For example, given the following tree:
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
We will use a recursive approach to flatten the binary tree. The idea is to recursively flatten the left and right subtrees, then append the right subtree to the end of the left subtree. This process is repeated until the entire tree is flattened.

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
        // Base case: if the tree is empty, return
        if (!root) return;
        
        // Recursively flatten the left and right subtrees
        flatten(root->left);
        flatten(root->right);
        
        // If the left subtree is not empty, append the right subtree to the end of the left subtree
        if (root->left) {
            // Find the rightmost node in the left subtree
            TreeNode* rightmost = root->left;
            while (rightmost->right) rightmost = rightmost->right;
            
            // Append the right subtree to the end of the left subtree
            rightmost->right = root->right;
            
            // Set the left child of the root to null and the right child to the left subtree
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
- The key to this problem is to understand how to recursively flatten a binary tree.
- We need to be careful when appending the right subtree to the end of the left subtree to avoid losing any nodes.
- The time complexity is O(N) because we visit each node once, and the space complexity is O(N) because of the recursive call stack.