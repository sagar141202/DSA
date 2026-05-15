# Symmetric Tree

## Problem Statement
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center). A binary tree is symmetric if it is the same when its left subtree is a mirror reflection of its right subtree. The tree only contains nodes with values 0-9, and each node has at most two children (i.e., left child and right child). For example, the binary tree `[1,2,2,null,3,null,3]` is symmetric, but the binary tree `[1,2,2,null,3,null,4]` is not symmetric.

## Approach
The approach to solve this problem is to use a recursive function that checks if the left subtree is a mirror of the right subtree. This can be done by checking if the values of the nodes at corresponding positions are equal and if the structure of the subtrees is also symmetric.

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
        if (root == NULL) return true;
        return isMirror(root->left, root->right);
    }

    bool isMirror(TreeNode* left, TreeNode* right) {
        if (left == NULL && right == NULL) return true;
        if (left == NULL || right == NULL) return false;
        return (left->val == right->val) && isMirror(left->right, right->left) && isMirror(left->left, right->right);
    }
};
```

## Test Cases
```
Input: [1,2,2,null,3,null,3]
Output: true
Input: [1,2,2,null,3,null,4]
Output: false
```

## Key Takeaways
- To check if a binary tree is symmetric, we need to check if its left subtree is a mirror of its right subtree.
- We can use a recursive function to check if two subtrees are mirrors of each other.
- The time complexity of this solution is O(N), where N is the number of nodes in the tree, because we visit each node once. The space complexity is O(H), where H is the height of the tree, because that's the maximum depth of the recursive call stack.