# Lowest Common Ancestor of BST

## Problem Statement
Given a binary search tree (BST) and two nodes in the tree, find the lowest common ancestor (LCA) of the two nodes. The LCA is the node furthest from the root that is an ancestor of both nodes. The BST is defined such that for any node, all elements in the left subtree are less than the node, and all elements in the right subtree are greater than the node. The nodes do not contain duplicate values.

## Approach
The algorithm works by traversing the BST from the root node, moving left or right based on whether the current node's value is greater than or less than the values of the two nodes. If the current node's value is between the two nodes, it is the LCA.

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
        // If the current node is NULL, return NULL
        if (root == NULL) return NULL;
        
        // If both p and q are less than the current node, move left
        if (p->val < root->val && q->val < root->val) {
            return lowestCommonAncestor(root->left, p, q);
        }
        
        // If both p and q are greater than the current node, move right
        if (p->val > root->val && q->val > root->val) {
            return lowestCommonAncestor(root->right, p, q);
        }
        
        // If the current node is between p and q, it is the LCA
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
- The LCA of two nodes in a BST can be found by traversing the tree from the root, moving left or right based on the values of the nodes.
- The time complexity of the algorithm is O(h), where h is the height of the tree, which can be O(log n) for a balanced tree or O(n) for an unbalanced tree.
- The space complexity of the algorithm is O(1), as it only uses a constant amount of space to store the current node and the two input nodes.