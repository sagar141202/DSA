# Lowest Common Ancestor of BST

## Problem Statement
Given a binary search tree (BST) and two nodes, find the lowest common ancestor (LCA) of the two nodes. The LCA is the node that is farthest from the root and is an ancestor of both nodes. The BST has the following properties: all values to the left of a node are less than the node's value, and all values to the right of a node are greater than the node's value. The input will consist of the root of the BST and the values of the two nodes. The output should be the value of the LCA.

## Approach
The algorithm works by traversing the BST from the root node, comparing the values of the current node with the values of the two input nodes. If the current node's value is greater than both input node values, we move to the left subtree. If the current node's value is less than both input node values, we move to the right subtree. Otherwise, the current node is the LCA.

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
        
        // If the root's value is greater than both p and q, move to the left subtree
        if (root->val > p->val && root->val > q->val) {
            return lowestCommonAncestor(root->left, p, q);
        }
        
        // If the root's value is less than both p and q, move to the right subtree
        if (root->val < p->val && root->val < q->val) {
            return lowestCommonAncestor(root->right, p, q);
        }
        
        // Otherwise, the root is the LCA
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
- The LCA of two nodes in a BST can be found by traversing the tree from the root and comparing the values of the current node with the values of the two input nodes.
- The time complexity of this algorithm is O(h), where h is the height of the tree, which can be O(log n) for a balanced BST or O(n) for an unbalanced BST.
- The space complexity of this algorithm is O(h), due to the recursive call stack.