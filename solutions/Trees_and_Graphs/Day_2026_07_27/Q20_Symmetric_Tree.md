# Symmetric Tree

## Problem Statement
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center). A binary tree is symmetric if it is the same when its left subtree is a mirror reflection of its right subtree. For example, the binary tree with the following structure is symmetric: 
     1
   /   \
  2     2
 / \   / \
3   4 4   3
However, the following is not symmetric:
    1
   / \
  2   2
   \   \
   3    3

## Approach
To determine if a binary tree is symmetric, we can compare the left subtree with the mirrored right subtree. This can be achieved by recursively checking if the left child of the left subtree is equal to the right child of the right subtree, and vice versa.

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
        if (root == NULL) {
            return true;
        }
        
        // Helper function to check symmetry
        return isMirror(root->left, root->right);
    }
    
    bool isMirror(TreeNode* left, TreeNode* right) {
        // Base case: both subtrees are empty
        if (left == NULL && right == NULL) {
            return true;
        }
        
        // If one subtree is empty and the other is not, they are not symmetric
        if (left == NULL || right == NULL) {
            return false;
        }
        
        // Recursively check if the subtrees are mirrors of each other
        return (left->val == right->val) && isMirror(left->left, right->right) && isMirror(left->right, right->left);
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
- Recursion can be used to compare the left and right subtrees.
- The time complexity of this solution is O(n), where n is the number of nodes in the tree, since we visit each node once.