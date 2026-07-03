# Symmetric Tree

## Problem Statement
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center). A binary tree is symmetric if it is the same when its left subtree is a mirror reflection of its right subtree. For example, the binary tree `[1,2,2,3,4,4,3]` is symmetric, but the binary tree `[1,2,2,null,3,null,3]` is not. The input binary tree will have up to 100 nodes, and each node will have a value between 0 and 99. The tree is represented as a binary tree where each node has a value and two children (left and right).

## Approach
The approach to solve this problem is to use a recursive function that checks if the left subtree is a mirror of the right subtree. This can be done by comparing the values of the nodes and their corresponding mirror nodes. If all pairs of nodes are mirrors of each other, then the tree is symmetric.

## Complexity
- Time: O(n)
- Space: O(n)

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
    bool isSymmetric(TreeNode* root) {
        // If the tree is empty, it is symmetric
        if (root == NULL) return true;

        // Call the helper function to check if the tree is symmetric
        return isMirror(root->left, root->right);
    }

    // Helper function to check if two trees are mirrors of each other
    bool isMirror(TreeNode* t1, TreeNode* t2) {
        // If both trees are empty, they are mirrors
        if (t1 == NULL && t2 == NULL) return true;

        // If one tree is empty and the other is not, they are not mirrors
        if (t1 == NULL || t2 == NULL) return false;

        // If the values of the nodes are not equal, the trees are not mirrors
        if (t1->val != t2->val) return false;

        // Recursively check if the left subtree of t1 is a mirror of the right subtree of t2
        // and if the right subtree of t1 is a mirror of the left subtree of t2
        return isMirror(t1->left, t2->right) && isMirror(t1->right, t2->left);
    }
};
```

## Test Cases
```
Input: [1,2,2,3,4,4,3]
Output: true
Input: [1,2,2,null,3,null,3]
Output: false
```

## Key Takeaways
- A binary tree is symmetric if its left subtree is a mirror of its right subtree.
- The `isMirror` function checks if two trees are mirrors of each other by comparing the values of the nodes and their corresponding mirror nodes.
- The time complexity of the solution is O(n), where n is the number of nodes in the tree, because each node is visited once.