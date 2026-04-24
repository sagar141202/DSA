# Symmetric Tree

## Problem Statement
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center). A binary tree is symmetric if the left subtree is a mirror reflection of the right subtree. For example, the binary tree `[1,2,2,3,4,4,3]` is symmetric because it is the same when its left and right subtrees are mirrored. However, the binary tree `[1,2,2,null,3,null,3]` is not symmetric.

## Approach
The approach to solve this problem involves checking if the left subtree is a mirror of the right subtree. This can be achieved by comparing the left subtree with the mirrored right subtree. The algorithm checks for symmetry by recursively comparing the values of the left and right child nodes.

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
        // base case: if the tree is empty, it is symmetric
        if (root == NULL) return true;
        
        // helper function to check if two trees are mirror images
        return isMirror(root->left, root->right);
    }
    
    // helper function to check if two trees are mirror images
    bool isMirror(TreeNode* t1, TreeNode* t2) {
        // base case: if both trees are empty, they are mirror images
        if (t1 == NULL && t2 == NULL) return true;
        
        // if one tree is empty and the other is not, they are not mirror images
        if (t1 == NULL || t2 == NULL) return false;
        
        // if the values of the current nodes are different, the trees are not mirror images
        if (t1->val != t2->val) return false;
        
        // recursively check if the left subtree of t1 is a mirror image of the right subtree of t2
        // and if the right subtree of t1 is a mirror image of the left subtree of t2
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
- To check if a binary tree is symmetric, compare the left subtree with the mirrored right subtree.
- Use a recursive approach to check if two trees are mirror images.
- The time complexity is O(n), where n is the number of nodes in the tree, and the space complexity is O(h), where h is the height of the tree.