# Diameter of Binary Tree

## Problem Statement
The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root. Given a binary tree, find the diameter of the tree. The diameter of a binary tree is the number of nodes in the longest path between any two nodes. For example, in the tree with nodes 1, 2, 3, 4, 5, the diameter is 3 (path: 4 -> 2 -> 1 -> 3 or 4 -> 2 -> 5).

## Approach
To solve this problem, we will use a depth-first search (DFS) approach to calculate the height of each subtree and keep track of the maximum diameter found so far. We will recursively calculate the height of the left and right subtrees and update the diameter if the sum of the heights of the left and right subtrees plus one is greater than the current diameter.

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
- The diameter of a binary tree can be calculated using a depth-first search (DFS) approach.
- We need to keep track of the maximum diameter found so far and update it if a longer path is found.
- The time complexity of this solution is O(N), where N is the number of nodes in the tree, and the space complexity is O(H), where H is the height of the tree.