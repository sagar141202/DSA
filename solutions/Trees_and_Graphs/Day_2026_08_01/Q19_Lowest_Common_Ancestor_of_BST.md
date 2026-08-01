# Lowest Common Ancestor of BST

## Problem Statement
Given a binary search tree (BST) and two nodes, find the lowest common ancestor (LCA) of the two nodes. The LCA is the node farthest from the root that is an ancestor of both nodes. The BST is defined such that for any node, all elements in its left subtree are less than the node, and all elements in its right subtree are greater than the node. The nodes do not contain duplicate values. For example, given a BST with the following structure:
       6
     /   \
    2     8
   / \   / \
  0   4 7   9
     / \
    3   5
The LCA of nodes 2 and 8 is 6. The LCA of nodes 2 and 4 is 2.

## Approach
We can solve this problem by traversing the BST from the root node and checking if the current node is greater than or equal to both nodes, or if it is less than or equal to both nodes. If it is greater than or equal to both, we move to the left subtree; otherwise, we move to the right subtree. We continue this process until we find a node that is the LCA of both nodes.

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
        // If the root is NULL, return NULL
        if (root == NULL) return NULL;
        
        // If both p and q are less than the root, move to the left subtree
        if (p->val < root->val && q->val < root->val) {
            return lowestCommonAncestor(root->left, p, q);
        }
        
        // If both p and q are greater than the root, move to the right subtree
        if (p->val > root->val && q->val > root->val) {
            return lowestCommonAncestor(root->right, p, q);
        }
        
        // If the root is the LCA of p and q, return the root
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
- The time complexity of this solution is O(h), where h is the height of the tree.
- The space complexity of this solution is O(h), where h is the height of the tree.