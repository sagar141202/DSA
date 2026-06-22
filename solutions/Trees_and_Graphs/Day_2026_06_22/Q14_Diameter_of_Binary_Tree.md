# Diameter of Binary Tree

## Problem Statement
Given a binary tree, find the length of the diameter of the tree, which is the longest path between any two nodes in the tree. This path may or may not pass through the root. The length of the path is the number of edges between the two nodes. The input is the root of the binary tree, and the output is the diameter of the tree. For example, given a binary tree with the following structure:
       1
      / \
     2   3
    / \
   4   5
The diameter of the tree is 3, which is the path between nodes 4 and 5.

## Approach
The approach is to use a depth-first search (DFS) to calculate the height of each node and update the diameter if the sum of the heights of the left and right subtrees is greater than the current diameter. The algorithm works by recursively calculating the height of each node and updating the diameter.

## Complexity
- Time: O(N)
- Space: O(H)

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
Input: [1,2,3,4,5]
Output: 3
```

## Key Takeaways
- The diameter of a binary tree is the longest path between any two nodes in the tree.
- The diameter can be calculated using a depth-first search (DFS) to calculate the height of each node and update the diameter if the sum of the heights of the left and right subtrees is greater than the current diameter.
- The time complexity of the algorithm is O(N), where N is the number of nodes in the tree, and the space complexity is O(H), where H is the height of the tree.