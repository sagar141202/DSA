# Lowest Common Ancestor of BST

## Problem Statement
Given a binary search tree (BST) and two nodes, find the lowest common ancestor (LCA) of the two nodes. The LCA is the node farthest from the root that is an ancestor of both nodes. The BST is defined such that for any node, all elements in the left subtree are less than the node, and all elements in the right subtree are greater than the node. The nodes do not contain duplicates.

## Approach
The approach involves traversing the BST from the root node, comparing the values of the current node with the two given nodes. If both nodes are less than the current node, we move to the left subtree; if both are greater, we move to the right subtree. The first node that is greater than or equal to one of the given nodes and less than or equal to the other is the LCA.

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
        // The current node is the LCA
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
- The LCA in a BST can be found by traversing the tree based on the relative values of the nodes.
- The time complexity depends on the height of the tree (O(h)), which can be O(log n) for a balanced BST or O(n) in the worst case for an unbalanced BST.
- The space complexity is O(1) since we only use a constant amount of space to store the nodes and do not use any data structures that scale with input size.