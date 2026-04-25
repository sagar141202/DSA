# Symmetric Tree

## Problem Statement
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center). A binary tree is symmetric if the left subtree is a mirror reflection of the right subtree. The tree is symmetric if for every node, the corresponding node on the other side of the center has the same value.

## Approach
To solve this problem, we can use a recursive approach by checking if the left subtree is a mirror of the right subtree. We will create a helper function to check if two trees are mirror images of each other.

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
Output: true
Input: [1,2,2,null,3,null,3]
Output: false
```

## Key Takeaways
- To check if a binary tree is symmetric, we need to check if the left subtree is a mirror of the right subtree.
- We can use a recursive approach to solve this problem by creating a helper function to check if two trees are mirror images of each other.
- The time complexity of this solution is O(n), where n is the number of nodes in the tree, and the space complexity is O(h), where h is the height of the tree.