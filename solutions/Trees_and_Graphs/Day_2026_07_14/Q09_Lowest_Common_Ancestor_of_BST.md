# Lowest Common Ancestor of BST

## Problem Statement
Given a binary search tree (BST) and two nodes, find the lowest common ancestor (LCA) of the two nodes. The LCA is the node farthest from the root that is an ancestor of both nodes. The BST is defined such that for any node, all elements in the left subtree are less than the node, and all elements in the right subtree are greater than the node. The nodes do not contain duplicates.

## Approach
The algorithm works by traversing the BST from the root node, moving left if both nodes are less than the current node, and moving right if both nodes are greater than the current node. If one node is less than the current node and the other is greater, the current node is the LCA.

## Complexity
- Time: O(h)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        // if both p and q are less than the current node, move left
        if (p->val < root->val && q->val < root->val) {
            return lowestCommonAncestor(root->left, p, q);
        }
        // if both p and q are greater than the current node, move right
        if (p->val > root->val && q->val > root->val) {
            return lowestCommonAncestor(root->right, p, q);
        }
        // if one is less than and the other is greater, the current node is the LCA
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
- The LCA of two nodes in a BST can be found by traversing the tree from the root.
- The time complexity is O(h), where h is the height of the tree, which can be O(log n) for a balanced BST or O(n) for an unbalanced BST.
- The space complexity is O(1) since we only use a constant amount of space to store the recursive call stack.