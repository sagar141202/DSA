# Invert Binary Tree

## Problem Statement
Invert a binary tree, where the left child of each node becomes the right child and vice versa. The function should take the root of the binary tree as input and return the root of the inverted binary tree. The binary tree node has an integer value and two pointers, left and right, representing the left and right child nodes. The tree can have any number of nodes, and the input tree is guaranteed to be a valid binary tree.

## Approach
To invert a binary tree, we can use a recursive approach by swapping the left and right child nodes of each internal node. We start with the root node and recursively call the function on its left and right child nodes.

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
- The key to solving this problem is to use recursion to traverse the tree and swap the child nodes.
- The time complexity is O(n) because we visit each node exactly once.
- The space complexity is O(h) because the maximum depth of the recursive call stack is equal to the height of the tree.