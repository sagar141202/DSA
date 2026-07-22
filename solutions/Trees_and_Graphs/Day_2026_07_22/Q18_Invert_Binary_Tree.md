# Invert Binary Tree

## Problem Statement
Given the root of a binary tree, invert the tree and return its root. Inverting a binary tree means swapping the left and right child nodes of each internal node. For example, given the following binary tree:
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
The approach to solve this problem is to use a recursive function that swaps the left and right child nodes of each internal node. This function will recursively traverse the tree, inverting the left and right subtrees. The base case for the recursion is when the current node is null.

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
- The time complexity of the solution is O(n), where n is the number of nodes in the tree, because each node is visited once.
- The space complexity of the solution is O(h), where h is the height of the tree, because of the recursive call stack. In the worst case, the tree is skewed and the space complexity is O(n).