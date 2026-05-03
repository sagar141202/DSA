# Symmetric Tree

## Problem Statement
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center). A binary tree is symmetric if the left subtree is a mirror reflection of the right subtree. For example, the following binary tree is symmetric: 
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
The function should return true if the tree is symmetric and false otherwise. The tree has at most 100 nodes, and each node has a value between 0 and 99.

## Approach
The algorithm checks if a binary tree is symmetric by comparing the left subtree with the mirrored right subtree. This can be achieved by using a recursive approach to compare nodes. The base case is when both trees are empty, in which case they are symmetric. If one tree is empty and the other is not, they are not symmetric.

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
        if (root == NULL) return true;
        
        // Helper function to check symmetry
        return isMirror(root->left, root->right);
    }
    
    // Helper function to check if two trees are mirror images
    bool isMirror(TreeNode* t1, TreeNode* t2) {
        // If both trees are empty, they are mirror images
        if (t1 == NULL && t2 == NULL) return true;
        
        // If one tree is empty and the other is not, they are not mirror images
        if (t1 == NULL || t2 == NULL) return false;
        
        // If the values of the nodes are different, the trees are not mirror images
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
- A binary tree is symmetric if the left subtree is a mirror reflection of the right subtree.
- The algorithm uses a recursive approach to compare nodes and determine symmetry.
- The time complexity is O(n), where n is the number of nodes in the tree, and the space complexity is O(h), where h is the height of the tree.