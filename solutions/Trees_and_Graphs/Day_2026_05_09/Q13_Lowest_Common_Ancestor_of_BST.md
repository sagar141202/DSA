# Lowest Common Ancestor of BST

## Problem Statement
Given a binary search tree (BST) and two nodes, find the lowest common ancestor (LCA) of the two nodes. The LCA is the node farthest from the root that is an ancestor of both nodes. The BST has the following properties: all values in the left subtree of a node are less than the value in the node, and all values in the right subtree of a node are greater than the value in the node. The nodes do not have parent pointers.

## Approach
The algorithm works by traversing the BST from the root node, comparing the values of the current node with the two given nodes. If both nodes have values less than the current node, we move to the left subtree. If both nodes have values greater than the current node, we move to the right subtree. Otherwise, the current node is the LCA.

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
- The LCA of two nodes in a BST can be found by traversing the tree from the root node.
- The algorithm has a time complexity of O(h), where h is the height of the tree.
- The algorithm has a space complexity of O(h), due to the recursive call stack.