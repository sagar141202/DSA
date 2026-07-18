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
The binary tree node has a value and two children, left and right.

## Approach
The algorithm involves recursively swapping the left and right children of each node in the binary tree. Start at the root, swap its children, and then recursively invert the left and right subtrees.

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
        if (root == NULL) return NULL;
        
        // Swap the left and right children
        TreeNode* temp = root->left;
        root->left = root->right;
        root->right = temp;
        
        // Recursively invert the left and right subtrees
        root->left = invertTree(root->left);
        root->right = invertTree(root->right);
        
        return root;
    }
};
```

## Test Cases
```
Input: 
    4
   / \
  2   7
 / \ / \
1  3 6  9
Output: 
    4
   / \
  7   2
 / \ / \
9  6 3  1
```

## Key Takeaways
- The key to solving this problem is to recognize that it can be solved recursively by swapping the left and right children of each node.
- The base case for the recursion is when the tree is empty (i.e., the root is NULL).
- The time complexity is O(n), where n is the number of nodes in the tree, because each node is visited once.