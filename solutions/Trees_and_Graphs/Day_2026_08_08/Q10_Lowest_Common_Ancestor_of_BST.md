# Lowest Common Ancestor of BST

## Problem Statement
Given a binary search tree (BST) and two nodes with values `p` and `q`, find the lowest common ancestor (LCA) of `p` and `q`. The LCA of two nodes is the node farthest from the root that is an ancestor of both nodes. The BST is guaranteed to be non-empty and `p` and `q` are guaranteed to be in the tree. The values of `p` and `q` are unique in the tree.

## Approach
The approach is to traverse the BST from the root node, comparing the values of `p` and `q` with the current node's value. If both `p` and `q` are less than the current node, move to the left subtree. If both `p` and `q` are greater than the current node, move to the right subtree. If `p` and `q` are on different sides of the current node, the current node is the LCA.

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
        // if both p and q are less than the current node, move to the left subtree
        if (p->val < root->val && q->val < root->val) {
            return lowestCommonAncestor(root->left, p, q);
        }
        // if both p and q are greater than the current node, move to the right subtree
        else if (p->val > root->val && q->val > root->val) {
            return lowestCommonAncestor(root->right, p, q);
        }
        // if p and q are on different sides of the current node, the current node is the LCA
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
- The LCA of two nodes in a BST can be found by traversing the tree from the root node.
- The time complexity is O(h), where h is the height of the tree, because in the worst case we need to traverse the entire height of the tree.
- The space complexity is O(h) due to the recursive call stack.