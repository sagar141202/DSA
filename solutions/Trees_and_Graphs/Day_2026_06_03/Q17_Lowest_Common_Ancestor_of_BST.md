# Lowest Common Ancestor of BST

## Problem Statement
Given a binary search tree (BST) and two nodes, find the lowest common ancestor (LCA) of the two nodes. The LCA is the node farthest from the root that is an ancestor of both nodes. The BST has the following properties: all nodes to the left of a node have values less than the node, and all nodes to the right of a node have values greater than the node. The nodes do not have parent pointers. For example, given the following BST:
       6
     /   \
    2     8
   / \   / \
  0   4 7   9
     / \
    3   5
The LCA of nodes 2 and 8 is 6, the LCA of nodes 2 and 4 is 2, and the LCA of nodes 3 and 5 is 4.

## Approach
We can solve this problem by using a recursive or iterative approach to traverse the BST, taking advantage of its properties to find the LCA. We start at the root and compare the values of the two nodes with the current node. If both nodes are less than the current node, we move to the left subtree; if both nodes are greater, we move to the right subtree. If one node is less and the other is greater, the current node is the LCA.

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
        // If one of p or q is less than the current node and the other is greater, 
        // the current node is the LCA
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
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 3, q = 5
Output: 4
```

## Key Takeaways
- The LCA of two nodes in a BST can be found by taking advantage of the BST properties.
- We can use a recursive or iterative approach to traverse the BST and find the LCA.
- The time complexity is O(h), where h is the height of the BST, and the space complexity is O(h) for the recursive call stack.