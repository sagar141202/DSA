# Invert Binary Tree

## Problem Statement
Given the root of a binary tree, invert the tree, and return its root. Inverting a binary tree means swapping the left and right child nodes of each internal node. The function should take the root of the binary tree as input and return the root of the inverted binary tree. For example, given the binary tree:
     4
   /   \
  2     7
 / \   / \
1   3 6   9
The inverted binary tree will be:
     4
   /   \
  7     2
 / \   / \
9   6 3   1

## Approach
To invert a binary tree, we can use a recursive approach where we swap the left and right child nodes of each internal node. We start by checking if the root is null, and if not, we recursively invert the left and right subtrees and then swap them.

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
    // Function to invert the binary tree
    TreeNode* invertTree(TreeNode* root) {
        // Base case: if the tree is empty, return null
        if (root == nullptr) {
            return nullptr;
        }
        
        // Recursively invert the left and right subtrees
        TreeNode* temp = root->left;
        root->left = invertTree(root->right);
        root->right = invertTree(temp);
        
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
- The time complexity of the solution is O(n), where n is the number of nodes in the binary tree, because we visit each node once.
- The space complexity of the solution is O(h), where h is the height of the binary tree, because that's the maximum depth of the recursive call stack.
- We use a recursive approach to invert the binary tree, which allows us to solve the problem in a clear and concise way.