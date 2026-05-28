# Symmetric Tree

## Problem Statement
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center). A binary tree is symmetric if it is the same when its left subtree is a mirror reflection of its right subtree. The tree only contains nodes with values 0-9. For example, the tree [1,2,2,null,3,null,3] is symmetric, but the tree [1,2,2,null,2,null,2] is not.

## Approach
The approach to solve this problem is to use a recursive function to check if the left subtree is a mirror of the right subtree. We can do this by comparing the values of the nodes at the same position in the left and right subtrees. If the values are equal and the structure of the subtrees is the same, then the tree is symmetric.

## Complexity
- Time: O(n)
- Space: O(h), where n is the number of nodes in the tree and h is the height of the tree.

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
        // base case: if the tree is empty, it is symmetric
        if (root == NULL) return true;
        
        // recursive function to check if two trees are mirror images
        return isMirror(root->left, root->right);
    }
    
    bool isMirror(TreeNode* t1, TreeNode* t2) {
        // base case: if both trees are empty, they are mirror images
        if (t1 == NULL && t2 == NULL) return true;
        
        // if one tree is empty and the other is not, they are not mirror images
        if (t1 == NULL || t2 == NULL) return false;
        
        // if the values of the nodes are not equal, the trees are not mirror images
        if (t1->val != t2->val) return false;
        
        // recursive calls to check the left and right subtrees
        return isMirror(t1->left, t2->right) && isMirror(t1->right, t2->left);
    }
};
```

## Test Cases
```
Input: [1,2,2,null,3,null,3]
Output: true
Input: [1,2,2,null,2,null,2]
Output: false
```

## Key Takeaways
- To check if a binary tree is symmetric, we need to compare the left and right subtrees.
- We can use a recursive function to compare the subtrees.
- The base cases for the recursion are when the trees are empty or when one tree is empty and the other is not.