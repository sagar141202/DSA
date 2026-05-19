# Invert Binary Tree

## Problem Statement
Invert a binary tree, where the left child of each node becomes the right child and vice versa. The function should take the root of the binary tree as input and return the root of the inverted binary tree. For example, given the following binary tree:
       4
     /   \
    2     7
   / \   / \
  1   3 6   9
The inverted binary tree would be:
       4
     /   \
    7     2
   / \   / \
  9   6 3   1
The binary tree nodes have the following structure: each node has a value and two children, left and right.

## Approach
The algorithm involves recursively traversing the binary tree and swapping the left and right children of each node. This can be achieved by using a recursive function that takes the root of the tree as input and returns the root of the inverted tree. The base case for the recursion is when the input tree is empty.

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
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    // Function to invert a binary tree
    TreeNode* invertTree(TreeNode* root) {
        // Base case: if the tree is empty, return NULL
        if (root == NULL) return NULL;
        
        // Swap the left and right children of the current node
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
- Recursive functions can be used to traverse and modify tree structures.
- Swapping the left and right children of each node is sufficient to invert a binary tree.
- The time complexity of the algorithm is proportional to the number of nodes in the tree, while the space complexity is proportional to the height of the tree.