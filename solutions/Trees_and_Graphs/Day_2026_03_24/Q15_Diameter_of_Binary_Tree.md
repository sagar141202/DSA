# Diameter of Binary Tree

## Problem Statement
The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root. The length of a path between two nodes is represented by the number of edges between them. Given a binary tree, find the diameter of the tree. The tree is represented by a TreeNode class, where each node has a value, a left child, and a right child. The diameter is calculated as the maximum number of edges between any two nodes. For example, in a tree with the following structure: 
       1
      / \
     2   3
    / \
   4   5
The diameter is 3, which is the path between nodes 4 and 5.

## Approach
To find the diameter of a binary tree, we can use a depth-first search (DFS) approach to calculate the height of each node. The diameter of the tree is the maximum diameter of each node, which is the sum of the heights of the left and right subtrees. We can calculate the height and diameter of each node recursively.

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
        dfs(root, diameter);
        return diameter;
    }
    
    int dfs(TreeNode* node, int& diameter) {
        if (!node) return 0;
        
        int leftHeight = dfs(node->left, diameter);
        int rightHeight = dfs(node->right, diameter);
        
        diameter = max(diameter, leftHeight + rightHeight);
        
        return max(leftHeight, rightHeight) + 1;
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
    / \
   4   5
  / \
 6   7
Output: 4
```

## Key Takeaways
- The diameter of a binary tree can be calculated using a DFS approach.
- The DFS function returns the height of each node and updates the diameter if a longer path is found.
- The time complexity is O(N), where N is the number of nodes in the tree, since we visit each node once.