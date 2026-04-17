# Lowest Common Ancestor of BST

## Problem Statement
Given a binary search tree (BST) and two nodes, find the lowest common ancestor (LCA) of the two nodes. The LCA is the node farthest from the root that is an ancestor of both nodes. The BST has the property that for any node, all elements in the left subtree are less than the node, and all elements in the right subtree are greater than the node. The nodes do not have a parent pointer.

## Approach
The algorithm works by traversing the BST from the root node, and at each step, it checks if the current node's value is greater than or equal to both nodes' values. If so, it moves to the left subtree; otherwise, it moves to the right subtree. This approach takes advantage of the BST property to find the LCA efficiently.

## Complexity
- Time: O(h)
- Space: O(1)

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
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        // If both p and q are less than the current node, move to the left subtree
        if (p->val < root->val && q->val < root->val) {
            return lowestCommonAncestor(root->left, p, q);
        }
        // If both p and q are greater than the current node, move to the right subtree
        if (p->val > root->val && q->val > root->val) {
            return lowestCommonAncestor(root->right, p, q);
        }
        // Otherwise, the current node is the LCA
        return root;
    }
};
```

## Test Cases
```
Input: 
     6
    / \
   2   8
  / \ / \
 0  4 7  9
  \ /
 3  5
p = 2, q = 8
Output: 6

Input: 
     6
    / \
   2   8
  / \ / \
 0  4 7  9
  \ /
 3  5
p = 2, q = 4
Output: 2
```

## Key Takeaways
- The LCA of two nodes in a BST can be found by traversing the tree from the root node.
- At each step, move to the left subtree if both nodes are less than the current node, and to the right subtree if both nodes are greater than the current node.
- The algorithm terminates when the current node is the LCA, which occurs when one node is less than or equal to the current node and the other node is greater than or equal to the current node.