# Lowest Common Ancestor of BST

## Problem Statement
Given the roots of two trees, find the lowest common ancestor (LCA) of the two trees in a Binary Search Tree (BST). The LCA of two nodes is the node farthest from the root that is an ancestor of both nodes. The BST has the property that for every node, all elements in the left subtree are less than the node and all elements in the right subtree are greater than the node. Both trees are non-empty and each node has a unique value.

## Approach
The algorithm uses a recursive approach, traversing the BST from the root node. It checks if the current node's value is greater than or equal to both p and q, in which case it moves to the left subtree. If the current node's value is less than or equal to both p and q, it moves to the right subtree. Otherwise, it returns the current node as the LCA.

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
        // if the current node is NULL, return NULL
        if (!root) return NULL;
        
        // if the current node's value is greater than both p and q, move to the left subtree
        if (root->val > p->val && root->val > q->val) {
            return lowestCommonAncestor(root->left, p, q);
        }
        
        // if the current node's value is less than both p and q, move to the right subtree
        if (root->val < p->val && root->val < q->val) {
            return lowestCommonAncestor(root->right, p, q);
        }
        
        // otherwise, return the current node as the LCA
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
- The LCA of two nodes in a BST is the node farthest from the root that is an ancestor of both nodes.
- The algorithm uses a recursive approach to traverse the BST and find the LCA.
- The time complexity of the algorithm is O(h), where h is the height of the BST.