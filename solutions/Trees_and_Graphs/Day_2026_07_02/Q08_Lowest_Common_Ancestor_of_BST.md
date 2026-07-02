# Lowest Common Ancestor of BST

## Problem Statement
Given a binary search tree (BST) and two nodes in the tree, find the lowest common ancestor (LCA) of the two nodes. The LCA is the node farthest from the root that is an ancestor of both nodes. The BST is defined such that for any node, all elements in the left subtree are less than the node, and all elements in the right subtree are greater than the node. The tree nodes have the following structure: `struct TreeNode { int val; TreeNode *left; TreeNode *right; TreeNode(int x) : val(x), left(NULL), right(NULL) {} };`. The function should take the root of the BST and the values of the two nodes as input and return the value of the LCA.

## Approach
The algorithm works by traversing the BST from the root, moving left or right based on the comparison of the current node's value with the values of the two nodes. If the current node's value is greater than both node values, we move left; if it's smaller than both, we move right. If the current node's value is between the two node values, it is the LCA.

## Complexity
- Time: O(h)
- Space: O(1)

## C++ Solution
```cpp
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        // if the current node is NULL, return NULL
        if (!root) return NULL;
        
        // if the current node's value is greater than both p and q's values, move left
        if (root->val > p->val && root->val > q->val) {
            return lowestCommonAncestor(root->left, p, q);
        }
        
        // if the current node's value is smaller than both p and q's values, move right
        if (root->val < p->val && root->val < q->val) {
            return lowestCommonAncestor(root->right, p, q);
        }
        
        // if the current node's value is between p and q's values, it is the LCA
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
- The LCA of two nodes in a BST can be found by traversing the tree from the root, moving left or right based on the comparison of the current node's value with the values of the two nodes.
- The time complexity of this solution is O(h), where h is the height of the tree, because in the worst case we might need to traverse from the root to a leaf node.
- The space complexity is O(1) because we only use a constant amount of space to store the current node and the two input nodes.