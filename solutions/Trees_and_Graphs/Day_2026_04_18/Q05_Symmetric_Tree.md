# Symmetric Tree

## Problem Statement
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center). A binary tree is symmetric if the left subtree is a mirror reflection of the right subtree. The definition of a mirror reflection is that for any two nodes at positions (x, y) and (x, -y) on the tree, their values must be equal. For example, the following binary tree is symmetric: 
       1
      / \
     2   2
    / \ / \
   3  4 4  3
But the following is not:
       1
      / \
     2   2
    / \   \
   3  4   3

## Approach
The approach is to use a recursive function to check if the left and right subtrees are mirror images of each other. We can do this by comparing the values of the nodes at corresponding positions in the left and right subtrees. If the values are equal, we recursively check the left child of the left subtree with the right child of the right subtree, and the right child of the left subtree with the left child of the right subtree.

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
        if (root == NULL) return true;
        return isMirror(root->left, root->right);
    }
    
    bool isMirror(TreeNode* t1, TreeNode* t2) {
        if (t1 == NULL && t2 == NULL) return true;
        if (t1 == NULL || t2 == NULL) return false;
        return (t1->val == t2->val) && isMirror(t1->left, t2->right) && isMirror(t1->right, t2->left);
    }
};
```

## Test Cases
```
Input: [1,2,2,3,4,4,3]
Output: True
Input: [1,2,2,null,3,null,3]
Output: False
```

## Key Takeaways
- A symmetric tree is a tree where the left subtree is a mirror reflection of the right subtree.
- The time complexity is O(n) because we visit each node once.
- The space complexity is O(h) because of the recursive call stack, where h is the height of the tree.