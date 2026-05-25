# Symmetric Tree

## Problem Statement
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center). A binary tree is symmetric if the left subtree is a mirror reflection of the right subtree. For example, the following binary tree is symmetric: 
     1
   /   \
  2     2
 / \   / \
3   4 4   3
However, the following is not symmetric:
     1
   /   \
  2     2
   \   \
   3    3

## Approach
The approach involves checking if the left subtree is a mirror of the right subtree by comparing their nodes recursively. We will use a helper function to check for symmetry. The algorithm checks if the trees are mirror images by comparing the left child of the left subtree with the right child of the right subtree and vice versa.

## Complexity
- Time: O(n)
- Space: O(h), where n is the number of nodes and h is the height of the tree

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
    
    // Helper function to check if two trees are mirror images
    bool isMirror(TreeNode* t1, TreeNode* t2) {
        // Base case: both trees are empty
        if (t1 == NULL && t2 == NULL) return true;
        
        // If one tree is empty and the other is not, they are not mirror images
        if (t1 == NULL || t2 == NULL) return false;
        
        // Check if the values of the nodes are equal and the left child of t1 is a mirror of the right child of t2 and vice versa
        return (t1->val == t2->val) && isMirror(t1->left, t2->right) && isMirror(t1->right, t2->left);
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
- To check if a binary tree is symmetric, we need to check if the left subtree is a mirror reflection of the right subtree.
- We can use a recursive approach to check for symmetry by comparing the nodes of the left and right subtrees.
- The time complexity of the solution is O(n), where n is the number of nodes in the tree, and the space complexity is O(h), where h is the height of the tree.