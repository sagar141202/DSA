# Invert Binary Tree

## Problem Statement
Given the root of a binary tree, invert the tree, and return its root. The inversion of a binary tree means swapping the left and right child nodes of each internal node. For example, given the following tree:
       4
     /   \
    2     7
   / \   / \
  1   3 6   9
The inverted tree would be:
       4
     /   \
    7     2
   / \   / \
  9   6 3   1
The function should take the root of the binary tree as input and return the root of the inverted tree.

## Approach
The algorithm involves recursively traversing the tree and swapping the left and right child nodes of each internal node. This can be achieved by using a recursive function that takes the root of the tree as input and returns the root of the inverted tree. The base case for the recursion is when the input tree is empty.

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
    // Function to invert a binary tree
    TreeNode* invertTree(TreeNode* root) {
        // Base case: if the tree is empty, return nullptr
        if (root == nullptr) {
            return nullptr;
        }
        
        // Swap the left and right child nodes
        TreeNode* temp = root->left;
        root->left = root->right;
        root->right = temp;
        
        // Recursively invert the left and right subtrees
        root->left = invertTree(root->left);
        root->right = invertTree(root->right);
        
        // Return the root of the inverted tree
        return root;
    }
};
```

## Test Cases
```
Input: [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
```

## Key Takeaways
- The inversion of a binary tree can be achieved by recursively swapping the left and right child nodes of each internal node.
- The time complexity of the algorithm is O(n), where n is the number of nodes in the tree, since each node is visited once.
- The space complexity of the algorithm is O(h), where h is the height of the tree, since the maximum depth of the recursion call stack is equal to the height of the tree.