# Symmetric Tree

## Problem Statement
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center). A binary tree is symmetric if it is the same when its left subtree is a mirror reflection of its right subtree. For example, the binary tree below is symmetric:
```
    1
   / \
  2   2
 / \ / \
3  4 4  3
```
However, the following binary tree is not symmetric:
```
    1
   / \
  2   2
   \   \
   3    3
```
The binary tree node has a value and two children (left and right). The function should return true if the tree is symmetric, and false otherwise.

## Approach
To check if a binary tree is symmetric, we can compare its left subtree with the mirror of its right subtree. We can use a recursive approach to check if two trees are mirror images of each other. If the values of the nodes are equal and the left subtree of the first tree is a mirror of the right subtree of the second tree, and the right subtree of the first tree is a mirror of the left subtree of the second tree, then the trees are symmetric.

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
        // if the tree is empty, it is symmetric
        if (root == NULL) return true;
        
        // check if the left subtree is a mirror of the right subtree
        return isMirror(root->left, root->right);
    }
    
    // helper function to check if two trees are mirror images of each other
    bool isMirror(TreeNode* t1, TreeNode* t2) {
        // if both trees are empty, they are mirror images
        if (t1 == NULL && t2 == NULL) return true;
        
        // if one tree is empty and the other is not, they are not mirror images
        if (t1 == NULL || t2 == NULL) return false;
        
        // if the values of the nodes are not equal, the trees are not mirror images
        if (t1->val != t2->val) return false;
        
        // check if the left subtree of the first tree is a mirror of the right subtree of the second tree
        // and the right subtree of the first tree is a mirror of the left subtree of the second tree
        return isMirror(t1->left, t2->right) && isMirror(t1->right, t2->left);
    }
};
```

## Test Cases
```
Input: 
    1
   / \
  2   2
 / \ / \
3  4 4  3
Output: true

Input: 
    1
   / \
  2   2
   \   \
   3    3
Output: false
```

## Key Takeaways
- To check if a binary tree is symmetric, we can compare its left subtree with the mirror of its right subtree.
- We can use a recursive approach to check if two trees are mirror images of each other.
- The time complexity of this solution is O(N), where N is the number of nodes in the tree, and the space complexity is O(H), where H is the height of the tree.