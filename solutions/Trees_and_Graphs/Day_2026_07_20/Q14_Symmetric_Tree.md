# Symmetric Tree

## Problem Statement
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center). A binary tree is symmetric if the left subtree is a mirror reflection of the right subtree. For example, the binary tree `[1,2,2,3,4,4,3]` is symmetric because it can be divided into two mirror-image halves. However, the binary tree `[1,2,2,null,3,null,3]` is not symmetric. The tree is empty if the root is `NULL`. The number of nodes in the tree will not exceed 1000.

## Approach
The approach to solve this problem is to use a recursive function that checks if two trees are mirror images of each other. We will recursively check the left subtree of the left half with the right subtree of the right half and vice versa. If all pairs of nodes have the same value, then the tree is symmetric.

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
        // If the tree is empty, it's symmetric
        if (root == NULL) return true;
        
        // Call the helper function to check if the tree is symmetric
        return isMirror(root->left, root->right);
    }
    
    // Helper function to check if two trees are mirror images
    bool isMirror(TreeNode* t1, TreeNode* t2) {
        // If both trees are empty, they are mirror images
        if (t1 == NULL && t2 == NULL) return true;
        
        // If one tree is empty and the other is not, they are not mirror images
        if (t1 == NULL || t2 == NULL) return false;
        
        // If the values are different, the trees are not mirror images
        if (t1->val != t2->val) return false;
        
        // Recursively check the left subtree of the left tree with the right subtree of the right tree
        // and the right subtree of the left tree with the left subtree of the right tree
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
- To check if a binary tree is symmetric, we can use a recursive function that checks if two trees are mirror images of each other.
- We need to handle the base cases where the trees are empty or have different values.
- The time complexity is O(n) where n is the number of nodes in the tree, and the space complexity is O(n) due to the recursive call stack.