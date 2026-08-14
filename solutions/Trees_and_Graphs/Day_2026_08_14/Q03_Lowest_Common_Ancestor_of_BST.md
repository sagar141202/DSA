# Lowest Common Ancestor of BST

## Problem Statement
Given a binary search tree (BST) and two nodes, find the lowest common ancestor (LCA) of the two nodes. The LCA is the node that is farthest from the root and is an ancestor of both nodes. The BST has the following properties: all nodes to the left of a node have values less than the node's value, and all nodes to the right of a node have values greater than the node's value. The nodes do not have parent pointers. For example, given a BST with the following structure:
       6
     /   \
    2     8
   / \   / \
  0   4 7   9
     / \
    3   5
And two nodes with values 2 and 8, the LCA is the node with value 6.

## Approach
The algorithm works by traversing the BST from the root node, and at each step, it checks if the current node's value is greater than both node values, in which case it moves to the left child, or if it's smaller than both, in which case it moves to the right child. If the current node's value is between the two node values, it's the LCA.

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
        // if the current node's value is greater than both p and q, move to the left child
        if (root->val > p->val && root->val > q->val) {
            return lowestCommonAncestor(root->left, p, q);
        }
        // if the current node's value is smaller than both p and q, move to the right child
        if (root->val < p->val && root->val < q->val) {
            return lowestCommonAncestor(root->right, p, q);
        }
        // if the current node's value is between p and q, it's the LCA
        return root;
    }
};
```

## Test Cases
```
Input: 
       6
     /   \
    2     8
   / \   / \
  0   4 7   9
     / \
    3   5
p = 2, q = 8
Output: 6

Input: 
       6
     /   \
    2     8
   / \   / \
  0   4 7   9
     / \
    3   5
p = 2, q = 4
Output: 2
```

## Key Takeaways
- The LCA of two nodes in a BST can be found by traversing the tree from the root and moving to the left or right child based on the current node's value.
- The time complexity is O(h), where h is the height of the tree, because in the worst case, we need to traverse from the root to the leaf node.
- The space complexity is O(h) due to the recursive call stack.