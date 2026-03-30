# Diameter of Binary Tree

## Problem Statement
The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root. Given a binary tree, find the length of the diameter of the tree. The length of the path is defined as the number of edges between the nodes. For example, the diameter of the binary tree with the following structure:
       1
      / \
     2   3
    / \
   4   5
is 3, which is the path between node 4 and node 5.

## Approach
The algorithm to solve this problem involves a depth-first search (DFS) to calculate the height of each node and update the diameter if a longer path is found. We will use a recursive approach to calculate the height of each node and update the diameter.

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
        if (node == NULL) {
            return 0;
        }
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
```

## Key Takeaways
- The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
- We can use DFS to calculate the height of each node and update the diameter if a longer path is found.
- The time complexity is O(N) and the space complexity is O(H), where N is the number of nodes in the tree and H is the height of the tree.