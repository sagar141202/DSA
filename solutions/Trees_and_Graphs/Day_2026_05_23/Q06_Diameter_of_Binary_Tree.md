# Diameter of Binary Tree

## Problem Statement
The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root. Given a binary tree, find the length of the diameter of the tree. The length of a path between two nodes is represented by the number of edges between them. For example, in the tree below, the diameter is 3 which is the path between node 4 and node 7 (4 -> 2 -> 1 -> 3 -> 7).

## Approach
The approach to solve this problem is to use a depth-first search (DFS) to calculate the height of each node and keep track of the maximum diameter found so far. We calculate the height of the left and right subtree for each node and update the diameter if the sum of the heights is greater than the current diameter.

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
```

## Key Takeaways
- The diameter of a binary tree can be calculated by finding the maximum sum of the heights of the left and right subtrees for each node.
- DFS is used to calculate the height of each node and update the diameter.
- The time complexity is O(N) where N is the number of nodes in the tree, and the space complexity is O(H) where H is the height of the tree.