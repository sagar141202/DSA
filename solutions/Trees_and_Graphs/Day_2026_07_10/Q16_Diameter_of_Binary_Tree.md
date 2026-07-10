# Diameter of Binary Tree

## Problem Statement
The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root. The length of a path between two nodes is represented by the number of edges between them. Given a binary tree, find the diameter of the binary tree. The binary tree node has an integer value, a left child, and a right child. For example, given the binary tree with the following structure: 
       1
      / \
     2   3
    / \     
   4   5    
The diameter of the binary tree is 3, which is the path between nodes 4, 2, and 5.

## Approach
To solve this problem, we will use a depth-first search (DFS) approach and calculate the height of each node. The diameter of the binary tree will be the maximum diameter found at any node, which is the sum of the heights of its left and right subtrees. 

## Complexity
- Time: O(N)
- Space: O(H), where N is the number of nodes and H is the height of the tree.

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
- Use DFS to calculate the height of each node and the diameter of the binary tree.
- Update the diameter whenever a larger diameter is found at any node.
- The time complexity is O(N), where N is the number of nodes in the binary tree.