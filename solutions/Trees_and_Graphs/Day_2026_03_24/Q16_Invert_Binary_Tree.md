# Invert Binary Tree

## Problem Statement
Given the root of a binary tree, invert the tree, and return its root. Inverting a binary tree means swapping the left and right child nodes of each internal node. The function should take the root of the binary tree as input and return the root of the inverted binary tree. For example, given the binary tree:
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
The approach is to use a recursive function to traverse the binary tree, swapping the left and right child nodes of each internal node. This can be achieved by using a Depth-First Search (DFS) traversal. The function will recursively call itself for the left and right subtrees, inverting them and then swapping the left and right child nodes.

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
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    TreeNode* invertTree(TreeNode* root) {
        // Base case: if the tree is empty, return nullptr
        if (root == nullptr) {
            return nullptr;
        }
        
        // Recursively invert the left and right subtrees
        TreeNode* temp = root->left;
        root->left = invertTree(root->right);
        root->right = invertTree(temp);
        
        // Return the root of the inverted tree
        return root;
    }
};
```

## Test Cases
```
Input: [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
```

## Key Takeaways
- The function uses a recursive approach to invert the binary tree.
- The time complexity is O(n), where n is the number of nodes in the tree, since each node is visited once.
- The space complexity is O(h), where h is the height of the tree, due to the recursive call stack.