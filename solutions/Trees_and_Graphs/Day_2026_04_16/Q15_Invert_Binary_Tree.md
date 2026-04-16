# Invert Binary Tree

## Problem Statement
Given the root of a binary tree, invert the tree and return its root. The inversion of a binary tree is done by swapping the left and right child nodes of each internal node. For example, given the following binary tree: 
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
The function should take the root of the original binary tree as input and return the root of the inverted binary tree.

## Approach
To invert a binary tree, we can use a recursive approach to traverse the tree and swap the left and right child nodes of each internal node. We start at the root node and recursively call the function on the left and right subtrees.

## Complexity
- Time: O(n)
- Space: O(h), where n is the number of nodes in the tree and h is the height of the tree

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
        
        // Swap the left and right child nodes
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
- The inversion of a binary tree can be done recursively by swapping the left and right child nodes of each internal node.
- The time complexity of the solution is O(n), where n is the number of nodes in the tree.
- The space complexity of the solution is O(h), where h is the height of the tree.