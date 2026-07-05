# Invert Binary Tree

## Problem Statement
Invert a binary tree, which means swapping the left and right child nodes of each internal node. Given the root of a binary tree, invert the tree and return its root. For example, given the following tree:
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
The function should take the root of the binary tree as input and return the root of the inverted binary tree.

## Approach
The approach to solve this problem is to use a recursive function that swaps the left and right child nodes of each internal node. The function will traverse the tree in a depth-first manner, inverting each subtree. This can be achieved by checking if the current node is null, and if not, recursively inverting its left and right subtrees and then swapping them.

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
Input: [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
Input: [2,1,3]
Output: [2,3,1]
```

## Key Takeaways
- Recursive functions can be used to solve tree-related problems by breaking down the problem into smaller sub-problems.
- The time complexity of the solution is linear, where n is the number of nodes in the tree.
- The space complexity of the solution is proportional to the height of the tree, which can be logarithmic in the best case (balanced tree) or linear in the worst case (unbalanced tree).