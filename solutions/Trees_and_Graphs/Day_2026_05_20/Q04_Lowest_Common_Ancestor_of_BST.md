# Lowest Common Ancestor of BST

## Problem Statement
Given a binary search tree (BST) and two nodes, find the lowest common ancestor (LCA) of the two nodes. The LCA is the node farthest from the root that is an ancestor of both nodes. The BST has the property that for any node, all elements in the left subtree are less than the node, and all elements in the right subtree are greater than the node. The input will consist of the root of the BST and the values of the two nodes.

## Approach
The algorithm works by traversing the BST from the root node, comparing the current node's value with the values of the two nodes. If the current node's value is greater than both node values, we move to the left subtree. If it's smaller than both, we move to the right subtree. Otherwise, the current node is the LCA.

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
        // if root is null, return null
        if (!root) return NULL;
        
        // if root's value is greater than both p and q, move to left subtree
        if (root->val > p->val && root->val > q->val) {
            return lowestCommonAncestor(root->left, p, q);
        }
        // if root's value is smaller than both p and q, move to right subtree
        if (root->val < p->val && root->val < q->val) {
            return lowestCommonAncestor(root->right, p, q);
        }
        // otherwise, root is the LCA
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
- The LCA of two nodes in a BST can be found in O(h) time, where h is the height of the tree.
- The algorithm takes advantage of the BST property to prune the search space.
- The recursive approach can be replaced with an iterative one for better performance.