# Symmetric Tree

## Problem Statement
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center). A binary tree is symmetric if it is the same when its left subtree is a mirror reflection of its right subtree. For example, the tree [1,2,2,null,3,null,3] is symmetric, but the tree [1,2,2,null,2,null,2] is not.

## Approach
To determine if a binary tree is symmetric, we can use a recursive approach to compare the left and right subtrees. We will check if the left subtree is a mirror of the right subtree by comparing the values of the nodes and their corresponding child nodes.

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
        // Base case: if the tree is empty, it is symmetric
        if (root == NULL) return true;
        
        // Recursive case: check if the left subtree is a mirror of the right subtree
        return isMirror(root->left, root->right);
    }
    
    bool isMirror(TreeNode* left, TreeNode* right) {
        // Base case: if both trees are empty, they are mirrors
        if (left == NULL && right == NULL) return true;
        
        // Base case: if one tree is empty and the other is not, they are not mirrors
        if (left == NULL || right == NULL) return false;
        
        // Recursive case: check if the values of the nodes are equal and the child nodes are mirrors
        return (left->val == right->val) && isMirror(left->left, right->right) && isMirror(left->right, right->left);
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
- A binary tree is symmetric if its left subtree is a mirror of its right subtree.
- We can use a recursive approach to compare the left and right subtrees and determine if the tree is symmetric.
- The time complexity of this solution is O(n), where n is the number of nodes in the tree, and the space complexity is O(h), where h is the height of the tree.