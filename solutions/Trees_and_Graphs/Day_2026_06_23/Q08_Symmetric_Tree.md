# Symmetric Tree

## Problem Statement
Given the root of a binary tree, check whether it is a mirror of itself (i.e., it is symmetric around its center). A binary tree is symmetric if the left subtree is a mirror reflection of the right subtree. For example, the binary tree `[1,2,2,null,3,null,3]` is symmetric, but the binary tree `[1,2,2,null,3,null]` is not.

## Approach
The algorithm checks for symmetry by comparing the left and right subtrees. It uses a recursive or iterative approach to compare the mirror images of the left and right subtrees. If the trees are mirror images, the function returns true; otherwise, it returns false.

## Complexity
- Time: O(n)
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
    bool isSymmetric(TreeNode* root) {
        // Base case: an empty tree is symmetric
        if (root == NULL) return true;
        
        // Helper function to check if two trees are mirror images
        return isMirror(root->left, root->right);
    }
    
    bool isMirror(TreeNode* t1, TreeNode* t2) {
        // Base case: two empty trees are mirror images
        if (t1 == NULL && t2 == NULL) return true;
        
        // If one tree is empty and the other is not, they are not mirror images
        if (t1 == NULL || t2 == NULL) return false;
        
        // Check if the values at the current nodes are equal
        // and if the left subtree of t1 is a mirror image of the right subtree of t2
        // and if the right subtree of t1 is a mirror image of the left subtree of t2
        return (t1->val == t2->val) && isMirror(t1->right, t2->left) && isMirror(t1->left, t2->right);
    }
};
```

## Test Cases
```
Input: [1,2,2,null,3,null,3]
Output: true
Input: [1,2,2,null,3,null]
Output: false
```

## Key Takeaways
- A binary tree is symmetric if its left subtree is a mirror reflection of its right subtree.
- The algorithm checks for symmetry by comparing the left and right subtrees using a recursive or iterative approach.
- The time complexity of the algorithm is O(n), where n is the number of nodes in the tree, and the space complexity is O(h), where h is the height of the tree.