# Symmetric Tree

## Problem Statement
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center). A binary tree is symmetric if the left subtree is a mirror reflection of the right subtree. The tree only contains nodes with values 0-9. For example, the following tree is symmetric: 
     1
   /   \
  2     2
 / \   / \
3   4 4   3
But the following tree is not symmetric:
     1
   /   \
  2     2
   \   /
   3  4

## Approach
To solve this problem, we can use a recursive approach to check if the left subtree is a mirror of the right subtree. We will compare the values of the nodes at corresponding positions in the left and right subtrees.

## Complexity
- Time: O(N)
- Space: O(H), where N is the number of nodes in the tree and H is the height of the tree

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    bool isSymmetric(TreeNode* root) {
        // Base case: if the tree is empty, it is symmetric
        if (root == nullptr) return true;
        
        // Call the helper function to check if the tree is symmetric
        return isMirror(root->left, root->right);
    }

    // Helper function to check if two trees are mirror images of each other
    bool isMirror(TreeNode* t1, TreeNode* t2) {
        // Base case: if both trees are empty, they are mirror images
        if (t1 == nullptr && t2 == nullptr) return true;
        
        // If one tree is empty and the other is not, they are not mirror images
        if (t1 == nullptr || t2 == nullptr) return false;
        
        // If the values of the nodes are not equal, the trees are not mirror images
        if (t1->val != t2->val) return false;
        
        // Recursively check if the left subtree of t1 is a mirror of the right subtree of t2
        // and if the right subtree of t1 is a mirror of the left subtree of t2
        return isMirror(t1->left, t2->right) && isMirror(t1->right, t2->left);
    }
};
```

## Test Cases
```
Input: 
     1
   /   \
  2     2
 / \   / \
3   4 4   3
Output: true

Input: 
     1
   /   \
  2     2
   \   /
   3  4
Output: false
```

## Key Takeaways
- To check if a binary tree is symmetric, we need to check if the left subtree is a mirror of the right subtree.
- We can use a recursive approach to solve this problem by comparing the values of the nodes at corresponding positions in the left and right subtrees.
- The time complexity of this solution is O(N), where N is the number of nodes in the tree, and the space complexity is O(H), where H is the height of the tree.