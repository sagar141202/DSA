# Lowest Common Ancestor of BST

## Problem Statement
Given a binary search tree (BST) and two nodes, find the lowest common ancestor (LCA) of the two nodes. The LCA of two nodes is the node farthest from the root that is an ancestor of both nodes. The BST is defined such that for any node, all elements in the left subtree are less than the node, and all elements in the right subtree are greater than the node. The nodes do not contain duplicate values.

## Approach
The approach involves traversing the BST from the root node, comparing the values of the current node with the two given nodes. If both nodes are less than the current node, we move to the left subtree; if both nodes are greater, we move to the right subtree. If one node is less and the other is greater, the current node is the LCA.

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
        else if (p->val > root->val && q->val > root->val) {
            return lowestCommonAncestor(root->right, p, q);
        }
        // If one of p or q is less than the current node and the other is greater, 
        // the current node is the LCA
        else {
            return root;
        }
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
- The LCA of two nodes in a BST can be found by traversing the tree from the root and comparing the node values.
- The time complexity of this solution is O(h), where h is the height of the tree, because in the worst case we might have to traverse from the root to the deepest leaf.
- The space complexity is O(h) due to the recursive call stack.