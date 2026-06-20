# Lowest Common Ancestor of BST

## Problem Statement
Given a binary search tree (BST) and two nodes with values p and q, find the lowest common ancestor (LCA) of p and q in the BST. The LCA of two nodes is the node farthest from the root that is an ancestor of both nodes. The BST is guaranteed to be non-empty, and both p and q are guaranteed to exist in the tree. For example, in the BST with the following structure:
       6
     /   \
    2     8
   / \   / \
  0   4 7   9
  / \
 3   5
The LCA of nodes 2 and 8 is 6, and the LCA of nodes 2 and 4 is 2.

## Approach
The algorithm works by traversing the BST from the root node, checking if the current node's value is greater than or equal to both p and q, or less than or equal to both p and q. If the current node's value is between p and q, it is the LCA. The traversal continues until the LCA is found.

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
        // If the current node's value is greater than both p and q, 
        // the LCA must be in the left subtree
        if (root->val > p->val && root->val > q->val) {
            return lowestCommonAncestor(root->left, p, q);
        }
        // If the current node's value is less than both p and q, 
        // the LCA must be in the right subtree
        if (root->val < p->val && root->val < q->val) {
            return lowestCommonAncestor(root->right, p, q);
        }
        // If the current node's value is between p and q, it is the LCA
        return root;
    }
};
```

## Test Cases
```
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
```

## Key Takeaways
- The LCA of two nodes in a BST can be found by traversing the tree from the root node.
- The traversal can be optimized by checking if the current node's value is greater than or equal to both p and q, or less than or equal to both p and q.
- The time complexity of the algorithm is O(h), where h is the height of the tree.