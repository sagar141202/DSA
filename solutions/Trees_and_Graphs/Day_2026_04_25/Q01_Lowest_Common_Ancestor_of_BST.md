# Lowest Common Ancestor of BST

## Problem Statement
Given a binary search tree (BST) and two nodes, find the lowest common ancestor (LCA) of the two nodes. The LCA is the node farthest from the root that is an ancestor of both nodes. The BST has the property that for every node, all elements in the left subtree are less than the node, and all elements in the right subtree are greater than the node. The nodes have unique values.

## Approach
We can solve this problem by traversing the BST from the root node and checking if the current node is greater than or equal to both nodes, or if it's less than both nodes. If it's greater than or equal to both, we move to the left subtree; otherwise, we move to the right subtree. We repeat this process until we find the LCA.

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
        
        // If the current node's value is greater than both p and q, move to the left subtree
        if (root->val > p->val && root->val > q->val) {
            return lowestCommonAncestor(root->left, p, q);
        }
        
        // If the current node's value is less than both p and q, move to the right subtree
        if (root->val < p->val && root->val < q->val) {
            return lowestCommonAncestor(root->right, p, q);
        }
        
        // If the current node's value is between p and q, it's the LCA
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
- The LCA of two nodes in a BST can be found by traversing the tree from the root and moving to the left or right subtree based on the values of the nodes.
- The time complexity of this solution is O(h), where h is the height of the tree, because in the worst case, we need to traverse from the root to the deepest leaf.
- The space complexity is O(1) because we only use a constant amount of space to store the current node and the two input nodes.