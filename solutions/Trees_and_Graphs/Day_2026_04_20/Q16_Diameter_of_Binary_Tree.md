# Diameter of Binary Tree

## Problem Statement
The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root. Given a binary tree, find the length of the diameter of the tree. The diameter of a tree is the number of edges in the longest path between any two nodes. For example, the diameter of the tree with the following structure: 
       1
      / \
     2   3
    / \     
   4   5
is 3, which is the path between 4 and 5.

## Approach
To find the diameter of a binary tree, we can use a depth-first search (DFS) approach to calculate the height of each node. The diameter of the tree is the maximum diameter of the left subtree, the right subtree, or the path through the current node.

## Complexity
- Time: O(N)
- Space: O(H), where N is the number of nodes in the tree and H is the height of the tree.

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
        
        int left = dfs(node->left, diameter);
        int right = dfs(node->right, diameter);
        
        diameter = max(diameter, left + right);
        
        return 1 + max(left, right);
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
  /
 6
Output: 4
```

## Key Takeaways
- Use DFS to calculate the height of each node and update the diameter.
- The diameter of the tree is the maximum diameter of the left subtree, the right subtree, or the path through the current node.
- Use a reference variable to update the diameter in the DFS function.