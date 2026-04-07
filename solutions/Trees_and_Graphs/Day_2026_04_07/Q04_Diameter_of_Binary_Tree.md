# Diameter of Binary Tree

## Problem Statement
Given a binary tree, find the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root. The length of a path between two nodes is represented by the number of edges between them. For example, in the binary tree with nodes 1, 2, 3, 4, 5, the diameter is 3, which is the path between nodes 4 and 5.

## Approach
To solve this problem, we will use a depth-first search (DFS) approach to find the height of each node and keep track of the maximum diameter found so far. We will calculate the height of the left and right subtrees for each node and update the diameter if the sum of the heights of the left and right subtrees is greater than the current diameter.

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
Output: 0
```

## Key Takeaways
- The diameter of a binary tree is the length of the longest path between any two nodes in the tree.
- We can use DFS to find the height of each node and keep track of the maximum diameter found so far.
- The time complexity of this solution is O(N), where N is the number of nodes in the tree, and the space complexity is O(H), where H is the height of the tree.