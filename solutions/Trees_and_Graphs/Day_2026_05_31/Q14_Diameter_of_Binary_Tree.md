# Diameter of Binary Tree

## Problem Statement
The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root. Given a binary tree, find the length of the diameter of the tree. The length of the path is the number of edges between the two nodes. For example, the diameter of the tree with the following structure:
       1
      / \
     2   3
    / \
   4   5
is 3, which is the path between node 4 and node 5.

## Approach
To find the diameter, we can calculate the height of the left and right subtrees for each node and update the diameter if the sum of these heights is greater than the current diameter. We use a recursive approach to traverse the tree and calculate the heights.

## Complexity
- Time: O(N)
- Space: O(H), where N is the number of nodes in the tree and H is the height of the tree

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
    int diameterOfBinaryTree(TreeNode* root) {
        int diameter = 0;
        diameterOfBinaryTreeHelper(root, diameter);
        return diameter;
    }
    
    int diameterOfBinaryTreeHelper(TreeNode* node, int& diameter) {
        if (node == NULL) {
            return 0;
        }
        int leftHeight = diameterOfBinaryTreeHelper(node->left, diameter);
        int rightHeight = diameterOfBinaryTreeHelper(node->right, diameter);
        diameter = max(diameter, leftHeight + rightHeight);
        return 1 + max(leftHeight, rightHeight);
    }
};
```

## Test Cases
```
Input: 
       1
      / \
     2   3
    / \
   4   5
Output: 3

Input: 
       1
      / \
     2   3
Output: 2
```

## Key Takeaways
- We use a recursive helper function to calculate the height of the left and right subtrees for each node.
- We update the diameter if the sum of the heights of the left and right subtrees is greater than the current diameter.
- The time complexity is O(N) because we visit each node once, and the space complexity is O(H) due to the recursive call stack.