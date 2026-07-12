# Lowest Common Ancestor of BST

## Problem Statement
Given a binary search tree (BST) and two nodes with values `p` and `q`, find the lowest common ancestor (LCA) of `p` and `q`. The LCA of two nodes is the node farthest from the root that is an ancestor of both nodes. The BST is guaranteed to be non-empty and the values of `p` and `q` are guaranteed to be in the tree. For example, given the following BST:
       6
     /   \
    2     8
   / \   / \
  0   4 7   9
     / \
    3   5
The LCA of nodes with values 2 and 8 is 6, and the LCA of nodes with values 2 and 4 is 2.

## Approach
The approach is to start at the root of the BST and traverse down the tree, at each step going to the left or right child based on whether the current node's value is greater than or less than the values of `p` and `q`. Since the tree is a BST, if the current node's value is greater than both `p` and `q`, we know that `p` and `q` must be in the left subtree. If the current node's value is less than both `p` and `q`, we know that `p` and `q` must be in the right subtree. If the current node's value is between `p` and `q`, we know that the current node is the LCA.

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
        // If the current node's value is greater than both p and q, go to the left subtree
        if (root->val > p->val && root->val > q->val) {
            return lowestCommonAncestor(root->left, p, q);
        }
        // If the current node's value is less than both p and q, go to the right subtree
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
Input: 
    6
   / \
  2   8
 / \ / \
0  4 7  9
   / \
  3   5
p = 2, q = 8
Output: 6
```

## Key Takeaways
- The key to solving this problem is to understand the properties of a binary search tree and how to use them to find the LCA of two nodes.
- The time complexity of this solution is O(h), where h is the height of the tree, because in the worst case we have to traverse from the root to a leaf node.
- The space complexity of this solution is O(h) because of the recursive call stack.