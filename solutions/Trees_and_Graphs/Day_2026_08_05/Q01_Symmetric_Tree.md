# Symmetric Tree

## Problem Statement
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center). A binary tree is symmetric if the left subtree is a mirror reflection of the right subtree. For example, the binary tree [1,2,2,3,4,4,3] is symmetric, but the binary tree [1,2,2,null,3,null,3] is not.

## Approach
To solve this problem, we can use a recursive approach by checking if the left subtree is a mirror of the right subtree. We can do this by comparing the left and right subtrees simultaneously. If they are mirror images, then the tree is symmetric.

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
        // Base case: if the tree is empty, it is symmetric
        if (root == NULL) return true;
        
        // Helper function to check if two trees are mirror images
        return isMirror(root->left, root->right);
    }
    
    bool isMirror(TreeNode* t1, TreeNode* t2) {
        // Base case: if both trees are empty, they are mirror images
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
- A binary tree is symmetric if the left subtree is a mirror reflection of the right subtree.
- We can use a recursive approach to check if a binary tree is symmetric by comparing the left and right subtrees simultaneously.
- The time complexity of this solution is O(N), where N is the number of nodes in the tree, and the space complexity is O(H), where H is the height of the tree.