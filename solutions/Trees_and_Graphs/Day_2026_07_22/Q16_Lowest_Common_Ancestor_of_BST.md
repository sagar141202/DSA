# Lowest Common Ancestor of BST

## Problem Statement
Given a binary search tree (BST) and two nodes, find the lowest common ancestor (LCA) of the two nodes. The LCA is the node that is farthest from the root and is an ancestor of both nodes. The BST has the following properties: all nodes to the left of a node have values less than the node's value, and all nodes to the right of a node have values greater than the node's value. The input will be the root of the BST and the values of the two nodes. The output will be the value of the LCA.

## Approach
The algorithm works by traversing the BST from the root, comparing the current node's value with the values of the two nodes. If the current node's value is greater than both node values, we move to the left subtree. If it's smaller than both, we move to the right subtree. If it's between the two values, the current node is the LCA.

## Complexity
- Time: O(h)
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
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        // If the current node's value is greater than both p's and q's values, 
        // the LCA must be in the left subtree
        if (root->val > p->val && root->val > q->val) {
            return lowestCommonAncestor(root->left, p, q);
        }
        // If the current node's value is smaller than both p's and q's values, 
        // the LCA must be in the right subtree
        if (root->val < p->val && root->val < q->val) {
            return lowestCommonAncestor(root->right, p, q);
        }
        // If the current node's value is between p's and q's values, 
        // the current node is the LCA
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
- The LCA of two nodes in a BST can be found by traversing the tree from the root.
- The algorithm takes advantage of the BST property to reduce the search space.
- The time complexity is O(h), where h is the height of the tree, which can be O(log n) for a balanced BST or O(n) for an unbalanced BST.