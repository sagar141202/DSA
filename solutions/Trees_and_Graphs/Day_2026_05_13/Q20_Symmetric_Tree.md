# Symmetric Tree

## Problem Statement
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center). A binary tree is symmetric if it is the same when its left subtree is a mirror reflection of its right subtree. For example, the tree [1,2,2,3,4,4,3] is symmetric, but the tree [1,2,2,null,3,null,3] is not. The tree is empty (i.e., null), which is symmetric.

## Approach
To solve this problem, we can use a recursive approach to compare the left and right subtrees. We can create a helper function to check if two trees are mirror images of each other. This function will recursively check if the values of the nodes are equal and if the left child of one tree is a mirror image of the right child of the other tree.

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
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    bool isSymmetric(TreeNode* root) {
        // If the tree is empty, it is symmetric
        if (root == nullptr) {
            return true;
        }
        
        // Call the helper function to check if the left and right subtrees are mirror images
        return isMirror(root->left, root->right);
    }
    
    // Helper function to check if two trees are mirror images
    bool isMirror(TreeNode* t1, TreeNode* t2) {
        // If both trees are empty, they are mirror images
        if (t1 == nullptr && t2 == nullptr) {
            return true;
        }
        
        // If one tree is empty and the other is not, they are not mirror images
        if (t1 == nullptr || t2 == nullptr) {
            return false;
        }
        
        // If the values of the nodes are not equal, the trees are not mirror images
        if (t1->val != t2->val) {
            return false;
        }
        
        // Recursively check if the left child of one tree is a mirror image of the right child of the other tree
        // and if the right child of one tree is a mirror image of the left child of the other tree
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
- The key to solving this problem is to create a helper function to check if two trees are mirror images of each other.
- The helper function should recursively check if the values of the nodes are equal and if the left child of one tree is a mirror image of the right child of the other tree.
- The time complexity of this solution is O(n), where n is the number of nodes in the tree, because we visit each node once. The space complexity is O(h), where h is the height of the tree, because that's the maximum depth of the recursive call stack.