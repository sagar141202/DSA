# Invert Binary Tree

## Problem Statement
Invert a binary tree, where the left child of each node becomes the right child and vice versa. The function should take the root of the binary tree as input and return the root of the inverted binary tree. For example, given the following binary tree:
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
The function should work for any binary tree with any number of nodes.

## Approach
The approach is to use a recursive function that swaps the left and right children of each node in the binary tree. This is done by first inverting the left and right subtrees and then swapping the left and right children of the current node.

## Complexity
- Time: O(n), where n is the number of nodes in the binary tree
- Space: O(h), where h is the height of the binary tree

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
    // Function to invert a binary tree
    TreeNode* invertTree(TreeNode* root) {
        // Base case: if the tree is empty
        if (root == NULL) {
            return NULL;
        }
        
        // Recursively invert the left and right subtrees
        TreeNode* temp = root->left;
        root->left = invertTree(root->right);
        root->right = invertTree(temp);
        
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
- The function uses recursion to invert the binary tree.
- The time complexity is O(n), where n is the number of nodes in the binary tree.
- The space complexity is O(h), where h is the height of the binary tree.