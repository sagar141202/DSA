# Diameter of Binary Tree

## Problem Statement
Given a binary tree, find the length of the diameter of the tree, which is the longest path between any two nodes in a tree. This path may or may not pass through the root. The length of the path is the number of edges between the two nodes. The diameter is the maximum length of the path. For example, in the binary tree with nodes 1, 2, 3, 4, and 5, the diameter is 3, which is the path between nodes 4 and 5.

## Approach
To find the diameter of a binary tree, we can calculate the height of the left and right subtrees for each node and keep track of the maximum diameter seen so far. We use a recursive approach to calculate the height of each subtree. The diameter of the tree is the maximum diameter seen during the recursion.

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
- The diameter of a binary tree can be calculated by finding the maximum diameter of the left and right subtrees for each node.
- The height of each subtree can be calculated recursively.
- The diameter is updated whenever a larger diameter is found during the recursion.