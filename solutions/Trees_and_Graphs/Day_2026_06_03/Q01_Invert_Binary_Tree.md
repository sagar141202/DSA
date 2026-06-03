# Invert Binary Tree

## Problem Statement
Given the root of a binary tree, invert the tree, and return its root. Inverting a binary tree means swapping the left and right child nodes of each internal node. For example, given the following tree:
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
The approach to solve this problem is to use a recursive function that traverses the binary tree and swaps the left and right child nodes of each internal node. The base case for the recursion is when the current node is null. The function will recursively call itself for the left and right child nodes after swapping them.

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
    TreeNode* invertTree(TreeNode* root) {
        // Base case: if the tree is empty, return null
        if (root == NULL) {
            return NULL;
        }
        
        // Swap the left and right child nodes
        TreeNode* temp = root->left;
        root->left = root->right;
        root->right = temp;
        
        // Recursively invert the left and right subtrees
        invertTree(root->left);
        invertTree(root->right);
        
        // Return the root of the inverted tree
        return root;
    }
};
```

## Test Cases
```
Input: 
       4
     /   \
    2     7
   / \   / \
  1   3 6   9
Output: 
       4
     /   \
    7     2
   / \   / \
  9   6 3   1
```

## Key Takeaways
- Recursion can be used to traverse and modify binary trees.
- Swapping the left and right child nodes of each internal node inverts the binary tree.
- The time complexity of the solution is O(n), where n is the number of nodes in the tree, and the space complexity is O(h), where h is the height of the tree.