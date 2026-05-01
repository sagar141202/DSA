# Invert Binary Tree

## Problem Statement
Invert a binary tree, where the left and right child nodes of each internal node are swapped. Given the root of a binary tree, return the root of the inverted binary tree. For example, given the binary tree:
     4
   /   \
  2     7
 / \   / \
1   3 6   9
The inverted binary tree is:
     4
   /   \
  7     2
 / \   / \
9   6 3   1
The function should take the root of the binary tree as input and return the root of the inverted binary tree.

## Approach
The algorithm to invert a binary tree involves recursively swapping the left and right child nodes of each internal node. This can be achieved by using a recursive function that takes the root of the tree as input and returns the root of the inverted tree.

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
- Recursive approach can be used to invert a binary tree by swapping the left and right child nodes of each internal node.
- The time complexity of the algorithm is O(n), where n is the number of nodes in the tree, since each node is visited once.
- The space complexity of the algorithm is O(h), where h is the height of the tree, due to the recursive call stack.