# Lowest Common Ancestor of BST

## Problem Statement
Given a binary search tree (BST) and two nodes, find the lowest common ancestor (LCA) of the two nodes. The LCA is the node farthest from the root that is an ancestor of both nodes. The BST has the following properties: all nodes to the left of a node have values less than the node's value, and all nodes to the right of a node have values greater than the node's value. The nodes do not have parent pointers.

## Approach
The algorithm works by traversing the BST from the root node, comparing the values of the current node with the values of the two given nodes. If both values are less than the current node's value, we move to the left subtree; if both values are greater, we move to the right subtree; otherwise, the current node is the LCA.

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
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
```

## Key Takeaways
- The LCA of two nodes in a BST can be found by traversing the tree from the root node.
- The time complexity of the algorithm is O(h), where h is the height of the tree.
- The space complexity of the algorithm is O(h), due to the recursive call stack.