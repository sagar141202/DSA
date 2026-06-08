# Diameter of Binary Tree

## Problem Statement
The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root. Given a binary tree, find the length of the diameter of the tree. The diameter of a binary tree is defined as the number of edges in the longest path between two nodes. For example, in the tree with the following structure: 
       1
      / \
     2   3
    / \     
   4   5    
The diameter is 3, which is the path between 4 and 5.

## Approach
The algorithm uses a depth-first search (DFS) approach to calculate the height of each subtree and update the diameter accordingly. It calculates the height of the left and right subtrees for each node and updates the diameter if the sum of the heights of the left and right subtrees is greater than the current diameter.

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
        if (node == NULL) return 0;
        
        int leftHeight = dfs(node->left, diameter);
        int rightHeight = dfs(node->right, diameter);
        
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
    / \
   4   5
  / \
 6   7
Output: 4
```

## Key Takeaways
- The diameter of a binary tree can be calculated using DFS.
- The height of each subtree is calculated and updated in the DFS function.
- The diameter is updated if the sum of the heights of the left and right subtrees is greater than the current diameter.