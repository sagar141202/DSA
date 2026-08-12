# Invert Binary Tree

## Problem Statement
Given the root of a binary tree, invert the tree, and return its root. Inverting a binary tree means swapping the left and right child nodes of each internal node. For example, given the binary tree:
```
    4
   / \
  2   7
 / \ / \
1  3 6  9
```
The inverted binary tree will be:
```
    4
   / \
  7   2
 / \ / \
9  6 3  1
```
The function should take the root of the binary tree as input and return the root of the inverted binary tree.

## Approach
The approach to solve this problem is to use a recursive function that traverses the binary tree and swaps the left and right child nodes of each internal node. This process is repeated until all nodes have been visited.

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
- The function uses a recursive approach to traverse the binary tree.
- The left and right child nodes of each internal node are swapped to invert the tree.
- The time complexity is O(n), where n is the number of nodes in the tree, since each node is visited once.