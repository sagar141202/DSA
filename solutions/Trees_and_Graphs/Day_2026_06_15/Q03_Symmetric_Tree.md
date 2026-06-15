# Symmetric Tree

## Problem Statement
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center). A binary tree is symmetric if it is the same when its left subtree is a mirror reflection of its right subtree. The tree is not necessarily a complete binary tree, and the height of the tree can vary. For example, given the following tree:     1
       / \
      2   2
     / \ / \
    3  4 4  3
   The function should return true because the tree is symmetric. However, for the following tree:     1
       / \
      2   2
       \   \
       3    3
   The function should return false because the tree is not symmetric.

## Approach
To solve this problem, we can use a recursive approach and check if the left subtree is a mirror of the right subtree. We can create a helper function that checks if two trees are mirror images of each other. This function will recursively check if the left child of the first tree is a mirror of the right child of the second tree and vice versa.

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
        if (root == NULL)
            return true;
        
        // call the helper function to check if the left and right subtrees are mirror images
        return isMirror(root->left, root->right);
    }
    
    // helper function to check if two trees are mirror images
    bool isMirror(TreeNode* t1, TreeNode* t2) {
        // if both trees are empty, they are mirror images
        if (t1 == NULL && t2 == NULL)
            return true;
        
        // if one tree is empty and the other is not, they are not mirror images
        if (t1 == NULL || t2 == NULL)
            return false;
        
        // if the values of the nodes are not equal, the trees are not mirror images
        if (t1->val != t2->val)
            return false;
        
        // recursively check if the left child of the first tree is a mirror of the right child of the second tree
        // and if the right child of the first tree is a mirror of the left child of the second tree
        return isMirror(t1->left, t2->right) && isMirror(t1->right, t2->left);
    }
};
```

## Test Cases
```
Input: 
    1
   / \
  2   2
 / \ / \
3  4 4  3
Output: true

Input: 
    1
   / \
  2   2
   \   \
   3    3
Output: false
```

## Key Takeaways
- The key to solving this problem is to create a helper function that checks if two trees are mirror images of each other.
- The helper function should recursively check if the left child of the first tree is a mirror of the right child of the second tree and vice versa.
- The base cases for the recursion are when both trees are empty (in which case they are mirror images) and when one tree is empty and the other is not (in which case they are not mirror images).