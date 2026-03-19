# Symmetric Tree

## Problem Statement
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center). A binary tree is symmetric if it is the same when its left subtree is a mirror reflection of its right subtree. For example, the binary tree `[1,2,2,3,4,4,3]` is symmetric, but the binary tree `[1,2,2,null,3,null,3]` is not.

## Approach
The approach is to use a recursive or iterative method to compare the left and right subtrees. We can use a helper function to check if two trees are mirror images of each other. If the trees are mirror images, then the original tree is symmetric.

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
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    bool isSymmetric(TreeNode* root) {
        // Base case: if the tree is empty, it is symmetric
        if (root == nullptr) return true;
        
        // Helper function to check if two trees are mirror images
        return isMirror(root->left, root->right);
    }
    
    bool isMirror(TreeNode* t1, TreeNode* t2) {
        // Base case: if both trees are empty, they are mirror images
        if (t1 == nullptr && t2 == nullptr) return true;
        // If one tree is empty and the other is not, they are not mirror images
        if (t1 == nullptr || t2 == nullptr) return false;
        
        // If the values of the nodes are not equal, the trees are not mirror images
        if (t1->val != t2->val) return false;
        
        // Recursively check the left subtree of t1 with the right subtree of t2
        // and the right subtree of t1 with the left subtree of t2
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
- A binary tree is symmetric if its left subtree is a mirror reflection of its right subtree.
- We can use a recursive or iterative method to compare the left and right subtrees.
- The time complexity of the solution is O(n), where n is the number of nodes in the tree, because we visit each node once.