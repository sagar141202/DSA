# Diameter of Binary Tree

## Problem Statement
The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root. Given a binary tree, find the diameter of the tree. The diameter of a tree is defined as the number of nodes along the longest path between any two nodes. For example, in the tree with the following structure:
       1
      / \
     2   3
    / \
   4   5
The diameter is 3 (path [4, 2, 1] or [5, 2, 1]).

## Approach
To find the diameter, we can use a depth-first search (DFS) approach to calculate the height of each node. The diameter is then the maximum sum of the heights of the left and right subtrees for any node. We will maintain a variable to keep track of the maximum diameter seen so far.

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
Input: [1,2,3,4,5]
Output: 3
```

## Key Takeaways
- The diameter of a binary tree can be found using a DFS approach.
- We need to calculate the height of each node and keep track of the maximum diameter seen so far.
- The time complexity is O(N) and the space complexity is O(H), where N is the number of nodes and H is the height of the tree.