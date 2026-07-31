# Symmetric Tree

## Problem Statement
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center). A binary tree is symmetric if the left subtree is a mirror reflection of the right subtree. The definition of a mirror is that for any two nodes at positions (x, y) and (x, -y) in the tree, their values should be equal, and their left and right child nodes should also be mirror images of each other. The binary tree has a maximum depth of 1000 nodes, and each node has a value between 0 and 9.

## Approach
To solve this problem, we can use a recursive approach to check if the left subtree is a mirror of the right subtree. We can create a helper function to check if two trees are mirror images of each other. This function will recursively check the values of the nodes and their child nodes.

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
        if (!root) return true;
        return isMirror(root->left, root->right);
    }
    
    bool isMirror(TreeNode* t1, TreeNode* t2) {
        if (!t1 && !t2) return true;
        if (!t1 || !t2) return false;
        return (t1->val == t2->val) && isMirror(t1->right, t2->left) && isMirror(t1->left, t2->right);
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
- Use recursive approach to check symmetry in binary trees.
- Create a helper function to check if two trees are mirror images of each other.
- Check the base cases where one or both of the trees are empty.