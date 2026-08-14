# Symmetric Tree

## Problem Statement
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center). A binary tree is symmetric if it is the same when its left subtree is a mirror reflection of its right subtree. For example, the following binary tree is symmetric: 
       1
      / \
     2   2
    / \ / \
   3  4 4  3
But the following is not: 
       1
      / \
     2   2
      \   \
       3    3

## Approach
To determine if a binary tree is symmetric, we can compare its left subtree with the mirror of its right subtree. This can be achieved by using a recursive or iterative approach to check for symmetry. We will use a recursive approach to solve this problem.

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
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    bool isSymmetric(TreeNode* root) {
        // If the tree is empty, it is symmetric
        if (root == NULL) return true;
        
        // Call the helper function to check for symmetry
        return isMirror(root->left, root->right);
    }
    
    // Helper function to check if two trees are mirror images
    bool isMirror(TreeNode* t1, TreeNode* t2) {
        // If both trees are empty, they are mirror images
        if (t1 == NULL && t2 == NULL) return true;
        
        // If one tree is empty and the other is not, they are not mirror images
        if (t1 == NULL || t2 == NULL) return false;
        
        // If the values at the current nodes are not equal, the trees are not mirror images
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
- We can use a recursive or iterative approach to check for symmetry in a binary tree.
- The time complexity of the solution is O(N), where N is the number of nodes in the tree, and the space complexity is O(H), where H is the height of the tree.