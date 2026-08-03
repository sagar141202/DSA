# Invert Binary Tree

## Problem Statement
Invert a binary tree, where the left and right child nodes of each internal node are swapped. Given the root of a binary tree, return the root of the inverted binary tree. For example, given the binary tree:
        4
       / \
      2   7
     / \ / \
    1  3 6  9
The inverted binary tree will be:
        4
       / \
      7   2
     / \ / \
    9  6 3  1
The function should handle an empty tree (i.e., a null root) and return null. The binary tree node has an integer value and two child pointers for the left and right children.

## Approach
To invert a binary tree, we will use a recursive approach where we swap the left and right child nodes of each internal node. We start from the root node and recursively call the function for the left and right subtrees.

## Complexity
- Time: O(n)
- Space: O(h), where n is the number of nodes in the tree and h is the height of the tree

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
    TreeNode* invertTree(TreeNode* root) {
        // Base case: if the tree is empty, return null
        if (root == nullptr) {
            return nullptr;
        }
        
        // Swap the left and right child nodes
        TreeNode* temp = root->left;
        root->left = root->right;
        root->right = temp;
        
        // Recursively call the function for the left and right subtrees
        invertTree(root->left);
        invertTree(root->right);
        
        return root;
    }
};
```

## Test Cases
```
Input: 
        4
       / \
      2   7
     / \ / \
    1  3 6  9
Output: 
        4
       / \
      7   2
     / \ / \
    9  6 3  1
Input: 
        2
       / \
      1   3
Output: 
        2
       / \
      3   1
```

## Key Takeaways
- The time complexity of the solution is O(n), where n is the number of nodes in the tree, since we visit each node once.
- The space complexity of the solution is O(h), where h is the height of the tree, due to the recursive call stack. In the worst case, the tree is skewed and h = n, resulting in a space complexity of O(n).