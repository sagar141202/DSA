# Symmetric Tree

## Problem Statement
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center). A binary tree is symmetric if the left subtree is a mirror reflection of the right subtree. The definition of a symmetric tree can also be stated as: two trees are mirror images of each other if and only if the following conditions are satisfied - The left subtree of the left tree and the right subtree of the right tree are mirror images of each other. The right subtree of the left tree and the left subtree of the right tree are mirror images of each other. The values of the corresponding nodes in the two trees are the same. For example, the following binary tree is symmetric: 
       1
      / \
     2   2
    / \ / \
   3  4 4  3
But the following is not:
       1
      / \
     2   2
    / \ / \
   3  4 3  4

## Approach
The approach is to check if the left subtree is a mirror of the right subtree. This can be done by creating a helper function to check for symmetry between two trees. The helper function checks if the values of the nodes are equal and if the left child of one tree is a mirror of the right child of the other tree, and vice versa.

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
        // if the tree is empty, it is symmetric
        if (root == NULL) return true;
        
        // call the helper function to check for symmetry
        return isMirror(root->left, root->right);
    }
    
    bool isMirror(TreeNode* t1, TreeNode* t2) {
        // if both trees are empty, they are mirror images
        if (t1 == NULL && t2 == NULL) return true;
        
        // if one tree is empty and the other is not, they are not mirror images
        if (t1 == NULL || t2 == NULL) return false;
        
        // if the values of the nodes are not equal, the trees are not mirror images
        if (t1->val != t2->val) return false;
        
        // recursively check the left subtree of the first tree with the right subtree of the second tree
        // and the right subtree of the first tree with the left subtree of the second tree
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
- To check if a binary tree is symmetric, we need to check if the left subtree is a mirror of the right subtree.
- We can use a helper function to check for symmetry between two trees.
- The helper function checks if the values of the nodes are equal and if the left child of one tree is a mirror of the right child of the other tree, and vice versa.