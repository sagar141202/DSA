# Invert Binary Tree

## Problem Statement
Invert a binary tree, where the left child of each node becomes the right child and vice versa. Given the root of a binary tree, return the root of the inverted binary tree. For example, given the binary tree:
       4
     /   \
    2     7
   / \   / \
  1   3 6   9
The inverted binary tree would be:
       4
     /   \
    7     2
   / \   / \
  9   6 3   1
The function should take the root of the binary tree as input and return the root of the inverted binary tree.

## Approach
The approach to solving this problem is to use a recursive function that swaps the left and right children of each node in the binary tree. This function will be called on the root of the tree and will recursively call itself on the left and right children of each node.

## Complexity
- Time: O(n)
- Space: O(h)

## C++ Solution
```cpp
#include <bits/stdc++.h>
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
    TreeNode* invertTree(TreeNode* root) {
        // Base case: if the tree is empty, return NULL
        if (root == NULL) {
            return NULL;
        }
        
        // Swap the left and right children of the current node
        TreeNode* temp = root->left;
        root->left = root->right;
        root->right = temp;
        
        // Recursively invert the left and right subtrees
        root->left = invertTree(root->left);
        root->right = invertTree(root->right);
        
        // Return the root of the inverted tree
        return root;
    }
};
```

## Test Cases
```
Input: 
       4
     /   \
    2     7
   / \   / \
  1   3 6   9
Output: 
       4
     /   \
    7     2
   / \   / \
  9   6 3   1
```

## Key Takeaways
- The function uses a recursive approach to invert the binary tree.
- The time complexity is O(n), where n is the number of nodes in the tree, since each node is visited once.
- The space complexity is O(h), where h is the height of the tree, since that is the maximum depth of the recursive call stack.