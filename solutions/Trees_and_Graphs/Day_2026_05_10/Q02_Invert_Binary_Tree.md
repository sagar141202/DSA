# Invert Binary Tree

## Problem Statement
Invert a binary tree, where the left child of every node becomes the right child and vice versa. The tree is defined by a root node, and each node has a value, a left child, and a right child. The input tree is guaranteed to be a valid binary tree. For example, given the binary tree:
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

## Approach
The approach to invert a binary tree is to recursively swap the left and right child nodes of each internal node. This can be achieved by using a recursive function that takes a node as an argument and swaps its children. The base case for the recursion is when the input node is null.

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
        // Base case: if the tree is empty, return null
        if (root == NULL) {
            return NULL;
        }
        
        // Recursively invert the left and right subtrees
        TreeNode* temp = root->left;
        root->left = invertTree(root->right);
        root->right = invertTree(temp);
        
        // Return the inverted tree
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
- Recursion can be used to solve tree problems by breaking down the problem into smaller sub-problems.
- The time complexity of tree traversals is usually O(n), where n is the number of nodes in the tree.
- The space complexity of recursive tree traversals is usually O(h), where h is the height of the tree.