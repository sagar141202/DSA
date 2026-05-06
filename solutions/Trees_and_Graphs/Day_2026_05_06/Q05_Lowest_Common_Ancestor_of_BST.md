# Lowest Common Ancestor of BST

## Problem Statement
Given the roots of two nodes in a Binary Search Tree (BST), find the Lowest Common Ancestor (LCA) of the two nodes. The LCA of two nodes is the node farthest from the root that is an ancestor of both nodes. The BST has the property that for every node, all elements in the left subtree are less than the node, and all elements in the right subtree are greater than the node. The nodes do not have a reference to their parent nodes.

## Approach
The algorithm works by traversing the BST from the root, at each step moving to the left subtree if both nodes are less than the current node, to the right subtree if both nodes are greater, and stopping when the current node is between the two nodes. This approach uses the properties of a BST to efficiently find the LCA.

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
- The LCA of two nodes in a BST can be found by traversing the tree from the root and using the properties of a BST to determine the direction of traversal.
- The time complexity of this approach is O(h), where h is the height of the tree, because in the worst case we need to traverse from the root to the deepest leaf.
- The space complexity is O(1) because we only use a constant amount of space to store the current node and the two input nodes.