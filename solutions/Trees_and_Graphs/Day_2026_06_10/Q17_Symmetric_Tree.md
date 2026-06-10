# Symmetric Tree

## Problem Statement
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center). A binary tree is symmetric if the left subtree is a mirror reflection of the right subtree. The definition of a mirror reflection is that for any two nodes at positions (x, y) and (x, -y) in the tree, their values are equal. The tree is symmetric if for any given node, its left child's value is equal to its right child's mirrored node's value, and the same goes for the structure of the tree. For example, the binary tree [1,2,2,3,4,4,3] is symmetric, but the binary tree [1,2,2,null,3,null,3] is not.

## Approach
To check if a binary tree is symmetric, we can use a recursive or iterative approach to compare the left and right subtrees. We can start from the root and recursively check if the left subtree is a mirror of the right subtree. The key idea is to compare the values and structure of the left and right subtrees.

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
        // Base case: an empty tree is symmetric
        if (root == NULL) return true;
        
        // Recursive function to check if two trees are mirror images
        return isMirror(root->left, root->right);
    }
    
    bool isMirror(TreeNode* t1, TreeNode* t2) {
        // Base case: both trees are empty
        if (t1 == NULL && t2 == NULL) return true;
        
        // If one tree is empty and the other is not, they are not mirror images
        if (t1 == NULL || t2 == NULL) return false;
        
        // Check if the values are equal and the left and right subtrees are mirror images
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
- A binary tree is symmetric if its left subtree is a mirror reflection of its right subtree.
- We can use a recursive or iterative approach to check if a binary tree is symmetric.
- The time complexity of the solution is O(N), where N is the number of nodes in the tree, and the space complexity is O(H), where H is the height of the tree.