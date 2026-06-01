# Flatten Binary Tree to Linked List

## Problem Statement
Given the root of a binary tree, flatten the tree into a linked list in-place. The linked list should be made by using the right child pointer and making the left child pointer as None. The resulting linked list should be in the same order as a pre-order traversal of the original binary tree. For example, given the following tree:
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
The approach to solve this problem is to perform a pre-order traversal of the binary tree and make the right child of each node point to the next node in the traversal order. We will use a recursive function to achieve this.

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
        flattenHelper(root);
    }
    
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
        
        // Return the tail of the flattened subtree
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
- The key to solving this problem is to understand how to perform a pre-order traversal of a binary tree and how to modify the tree to create a linked list.
- The recursive function `flattenHelper` is used to flatten the left and right subtrees and then append them to the current node.
- The `flatten` function is used to initiate the flattening process by calling the `flattenHelper` function on the root node.