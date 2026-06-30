# Diameter of Binary Tree

## Problem Statement
The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root. Given a binary tree, find the length of the diameter of the tree. The diameter of a tree is the number of edges in the longest path between any two nodes. For example, the diameter of the tree below is 3, which is the path between node 4 and node 7 (4 -> 2 -> 1 -> 3 -> 7). The path can be from any node to any other node, and it doesn't have to go through the root.

## Approach
We will use a depth-first search (DFS) approach to calculate the height of each node and keep track of the maximum diameter found so far. The diameter of a tree is the maximum value of (left_height + right_height + 1) for each node. We will use a recursive function to calculate the height of each node and update the diameter if necessary.

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
        
        int left_height = dfs(node->left, diameter);
        int right_height = dfs(node->right, diameter);
        
        diameter = max(diameter, left_height + right_height);
        
        return 1 + max(left_height, right_height);
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
Output: 3
```

## Key Takeaways
- The diameter of a tree can be calculated using a depth-first search (DFS) approach.
- We need to keep track of the maximum diameter found so far and update it if necessary.
- The time complexity of the solution is O(N), where N is the number of nodes in the tree, and the space complexity is O(H), where H is the height of the tree.