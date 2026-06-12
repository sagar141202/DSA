# Lowest Common Ancestor of BST

## Problem Statement
Given a binary search tree (BST) and two nodes, find the lowest common ancestor (LCA) of the two nodes. The LCA is the node farthest from the root that is an ancestor of both nodes. The BST has the property that for every node, all elements in the left subtree are less than the node, and all elements in the right subtree are greater than the node. The input consists of the root of the BST and the values of the two nodes. The output should be the value of the LCA node.

## Approach
The approach to solving this problem is to use the properties of a BST to find the LCA. We can start at the root and traverse the tree, moving left or right based on the values of the two nodes. If both nodes are less than the current node, we move left. If both nodes are greater than the current node, we move right. If one node is less than the current node and the other is greater, the current node is the LCA.

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
        // If both p and q are less than the current node, move left
        if (p->val < root->val && q->val < root->val) {
            return lowestCommonAncestor(root->left, p, q);
        }
        // If both p and q are greater than the current node, move right
        if (p->val > root->val && q->val > root->val) {
            return lowestCommonAncestor(root->right, p, q);
        }
        // If one node is less than the current node and the other is greater, the current node is the LCA
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
- The LCA of two nodes in a BST can be found by traversing the tree based on the values of the two nodes.
- The time complexity is O(h), where h is the height of the tree, because in the worst case we need to traverse from the root to the deepest leaf.
- The space complexity is O(h) because of the recursive call stack.