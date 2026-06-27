# Lowest Common Ancestor of BST

## Problem Statement
Given a binary search tree (BST) and two nodes, find the lowest common ancestor (LCA) of the two nodes. The LCA is the node farthest from the root that is an ancestor of both nodes. The BST has the following properties: all nodes to the left of a node have values less than the node's value, and all nodes to the right of a node have values greater than the node's value. The input will consist of the root of the BST and the values of the two nodes.

## Approach
The algorithm works by traversing the BST from the root, checking if the current node's value is greater than or equal to both node values. If it is, we move to the left subtree; otherwise, we move to the right subtree. This process continues until we find the LCA.

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
        // Otherwise, the current node is the LCA
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
p = 2, q = 8
Output: 6

Input: 
     6
   /   \
  2     8
 / \   / \
0   4 7   9
p = 2, q = 4
Output: 2
```

## Key Takeaways
- The LCA of two nodes in a BST is the node farthest from the root that is an ancestor of both nodes.
- We can use a recursive approach to find the LCA by traversing the BST from the root.
- The time complexity is O(h), where h is the height of the BST, and the space complexity is O(h) due to the recursive call stack.