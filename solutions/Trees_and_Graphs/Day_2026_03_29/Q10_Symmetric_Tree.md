# Symmetric Tree

## Problem Statement
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center). A binary tree is symmetric if the left subtree is a mirror reflection of the right subtree. The tree is considered symmetric if for each node at position (i, j), there is a node at position (i, -j) with the same value. The root node is at position (0, 0). The left child of a node at position (i, j) is at position (i + 1, j - 1), and the right child is at position (i + 1, j + 1).

## Approach
We can solve this problem by recursively checking if the left subtree is a mirror of the right subtree. This can be done by comparing the values of the left and right subtrees and their structures.

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
        // If the tree is empty, it is symmetric
        if (!root) return true;
        
        // Call the helper function to check symmetry
        return isMirror(root->left, root->right);
    }
    
    // Helper function to check if two trees are mirror images
    bool isMirror(TreeNode* t1, TreeNode* t2) {
        // If both trees are empty, they are mirror images
        if (!t1 && !t2) return true;
        
        // If one tree is empty and the other is not, they are not mirror images
        if (!t1 || !t2) return false;
        
        // If the values of the nodes are not equal, the trees are not mirror images
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
- The problem can be solved recursively by comparing the values and structures of the left and right subtrees.
- The time complexity of the solution is O(n), where n is the number of nodes in the tree, and the space complexity is O(h), where h is the height of the tree.