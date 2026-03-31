# Lowest Common Ancestor of BST

## Problem Statement
Given a binary search tree (BST) and two nodes, find the lowest common ancestor (LCA) of the two nodes. The LCA is the node that is farthest from the root and is an ancestor of both nodes. The BST has the following properties: all nodes to the left of a node have values less than the node's value, and all nodes to the right of a node have values greater than the node's value. For example, given a BST with nodes 6, 2, 8, 0, 4, 7, 9, and two nodes 2 and 8, the LCA is 6.

## Approach
The approach is to traverse the BST from the root, comparing the values of the current node with the values of the two nodes. If the current node's value is greater than both nodes' values, we move to the left subtree. If the current node's value is less than both nodes' values, we move to the right subtree. If the current node's value is between the two nodes' values, it is the LCA.

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
        // if the current node's value is greater than both p and q, move to the left subtree
        if (root->val > p->val && root->val > q->val) {
            return lowestCommonAncestor(root->left, p, q);
        }
        // if the current node's value is less than both p and q, move to the right subtree
        if (root->val < p->val && root->val < q->val) {
            return lowestCommonAncestor(root->right, p, q);
        }
        // if the current node's value is between p and q, it is the LCA
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
p = 2, q = 8
Output: 6

Input: 
     6
   /   \
  2     8
   \   / \
    4 7   9
p = 2, q = 4
Output: 2
```

## Key Takeaways
- The LCA of two nodes in a BST can be found by traversing the tree from the root and comparing the values of the current node with the values of the two nodes.
- The time complexity of this approach is O(h), where h is the height of the BST.
- The space complexity of this approach is O(1), as we only use a constant amount of space to store the current node and the two nodes.