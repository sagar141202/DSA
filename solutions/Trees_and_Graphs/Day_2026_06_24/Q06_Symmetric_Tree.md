# Symmetric Tree

## Problem Statement
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center). A binary tree is symmetric if it is the same when its left subtree is a mirror reflection of its right subtree. The tree only contains nodes with values 0-9. For example, the tree [1,2,2,null,3,null,3] is symmetric, while the tree [1,2,2,null,2,null,2] is not.

## Approach
To determine if a binary tree is symmetric, we can use a recursive approach to compare the left and right subtrees. We will check if the left subtree is a mirror image of the right subtree. If they are mirror images, the tree is symmetric.

## Complexity
- Time: O(N)
- Space: O(H)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    // Function to check if two trees are mirror images
    bool isMirror(TreeNode* t1, TreeNode* t2) {
        // If both trees are empty, they are mirror images
        if (t1 == nullptr && t2 == nullptr) return true;
        // If one tree is empty and the other is not, they are not mirror images
        if (t1 == nullptr || t2 == nullptr) return false;
        // If the values of the nodes are not equal, they are not mirror images
        if (t1->val != t2->val) return false;
        // Recursively check the left subtree of t1 with the right subtree of t2
        // and the right subtree of t1 with the left subtree of t2
        return isMirror(t1->left, t2->right) && isMirror(t1->right, t2->left);
    }

    bool isSymmetric(TreeNode* root) {
        // If the tree is empty, it is symmetric
        if (root == nullptr) return true;
        // Check if the left subtree is a mirror image of the right subtree
        return isMirror(root->left, root->right);
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
- The key to solving this problem is to understand the concept of a mirror image in the context of binary trees.
- We can use a recursive approach to compare the left and right subtrees.
- The time complexity is O(N), where N is the number of nodes in the tree, and the space complexity is O(H), where H is the height of the tree.