# Symmetric Tree

## Problem Statement
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center). A binary tree is symmetric if the left subtree is a mirror reflection of the right subtree. The definition of a mirror reflection is that for any two nodes at positions (x, y) and (x, -y) in the tree, their values are equal. For example, the following binary tree is symmetric: 
     1
   /   \
  2     2
 / \   / \
3   4 4   3
But the following is not:
     1
   /   \
  2     2
   \   /
   3  3

## Approach
We can solve this problem using recursion by comparing the left and right subtrees. The algorithm checks if the tree is symmetric by verifying if the left subtree is a mirror of the right subtree. This is done by comparing the values of the nodes at corresponding positions in the left and right subtrees.

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
        if (root == NULL) {
            return true;
        }
        
        // Call the helper function to check if the left and right subtrees are mirrors
        return isMirror(root->left, root->right);
    }
    
    // Helper function to check if two trees are mirrors
    bool isMirror(TreeNode* left, TreeNode* right) {
        // Base case: if both trees are empty, they are mirrors
        if (left == NULL && right == NULL) {
            return true;
        }
        
        // If one tree is empty and the other is not, they are not mirrors
        if (left == NULL || right == NULL) {
            return false;
        }
        
        // Check if the values of the nodes are equal and if the left and right subtrees are mirrors
        return (left->val == right->val) && isMirror(left->left, right->right) && isMirror(left->right, right->left);
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
- The key to solving this problem is to use recursion to compare the left and right subtrees.
- We need to define a helper function to check if two trees are mirrors.
- The time complexity is O(N), where N is the number of nodes in the tree, because we visit each node once.
- The space complexity is O(H), where H is the height of the tree, because that's the maximum depth of the recursion call stack.