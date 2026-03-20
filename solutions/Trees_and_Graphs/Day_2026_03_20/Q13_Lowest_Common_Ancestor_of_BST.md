# Lowest Common Ancestor of BST

## Problem Statement
Given the roots of two nodes in a Binary Search Tree (BST), find the Lowest Common Ancestor (LCA) of the two nodes. The LCA is the node farthest from the root that is an ancestor of both nodes. The BST is a binary tree where for each node, all elements in the left subtree are less than the node, and all elements in the right subtree are greater than the node. The input nodes are guaranteed to be in the tree and the tree is non-empty.

## Approach
The algorithm works by traversing the tree from the root, checking if the current node is greater than both input nodes, less than both, or between them. If the current node is greater than both, we move to the left subtree. If it's less than both, we move to the right subtree. If it's between them, it's the LCA.

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
        // if the current node is greater than both p and q, move to the left subtree
        if (root->val > p->val && root->val > q->val) {
            return lowestCommonAncestor(root->left, p, q);
        }
        // if the current node is less than both p and q, move to the right subtree
        if (root->val < p->val && root->val < q->val) {
            return lowestCommonAncestor(root->right, p, q);
        }
        // if the current node is between p and q, it's the LCA
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
p = 2, q = 8
Output: 6

Input: 
     6
    / \
   2   8
  / \ / \
 0  4 7  9
p = 2, q = 4
Output: 2
```

## Key Takeaways
- The key to solving this problem is to understand the properties of a Binary Search Tree.
- We can take advantage of the BST property to find the LCA in O(h) time, where h is the height of the tree.
- The recursive solution is straightforward and easy to implement, but an iterative solution is also possible.