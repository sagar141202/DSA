# Lowest Common Ancestor of BST

## Problem Statement
Given a binary search tree (BST) and two nodes, find the lowest common ancestor (LCA) of the two nodes. The LCA is the node farthest from the root that is an ancestor of both nodes. The BST is defined such that for any node, all elements in the left subtree are less than the node, and all elements in the right subtree are greater than the node. The nodes do not have a parent pointer, and the tree is non-empty.

## Approach
The algorithm works by traversing the BST from the root node, comparing the current node's value with the two given node values. If both values are less than the current node, we move to the left subtree; if both are greater, we move to the right subtree. If one is less and one is greater, the current node is the LCA.

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
    // function to find the LCA of two nodes in a BST
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        // if both p and q are less than the current node, move to the left subtree
        if (p->val < root->val && q->val < root->val) {
            return lowestCommonAncestor(root->left, p, q);
        }
        // if both p and q are greater than the current node, move to the right subtree
        if (p->val > root->val && q->val > root->val) {
            return lowestCommonAncestor(root->right, p, q);
        }
        // if one is less and one is greater, the current node is the LCA
        return root;
    }
};
```

## Test Cases
```
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
```

## Key Takeaways
- The LCA of two nodes in a BST can be found by traversing the tree from the root and comparing the node values.
- The time complexity of this solution is O(h), where h is the height of the tree, because in the worst-case scenario, we might need to traverse from the root to a leaf node.
- The space complexity is O(1) if we consider the recursive call stack space as O(1) for the iterative solution, but for the recursive solution, it would be O(h) due to the call stack.