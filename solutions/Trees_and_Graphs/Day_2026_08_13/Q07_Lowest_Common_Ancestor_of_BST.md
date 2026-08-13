# Lowest Common Ancestor of BST

## Problem Statement
Given a binary search tree (BST) and two nodes, find the lowest common ancestor (LCA) of the two nodes. The LCA is the node farthest from the root that is an ancestor of both nodes. The BST is defined such that for any node, all elements in the left subtree are less than the node, and all elements in the right subtree are greater than the node. For example, given a BST with nodes 6, 2, 8, 0, 4, 7, 9, and two nodes 2 and 8, the LCA is 6.

## Approach
We can solve this problem by traversing the BST from the root node and checking if the current node is greater than or equal to both target nodes, or less than or equal to both target nodes. If the current node is greater than or equal to both target nodes, we move to the left subtree. If the current node is less than or equal to both target nodes, we move to the right subtree. Otherwise, the current node is the LCA.

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
        // If the current node is NULL, return NULL
        if (root == NULL) return NULL;
        
        // If the current node's value is greater than both p's and q's values, move to the left subtree
        if (root->val > p->val && root->val > q->val) {
            return lowestCommonAncestor(root->left, p, q);
        }
        
        // If the current node's value is less than both p's and q's values, move to the right subtree
        if (root->val < p->val && root->val < q->val) {
            return lowestCommonAncestor(root->right, p, q);
        }
        
        // Otherwise, the current node is the LCA
        return root;
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
- The LCA of two nodes in a BST can be found by traversing the tree from the root node.
- The time complexity of this solution is O(h), where h is the height of the tree.
- The space complexity of this solution is O(h), due to the recursive call stack.