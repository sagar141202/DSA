# Diameter of Binary Tree

## Problem Statement
The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root. Given a binary tree, find the length of the diameter of the tree. The diameter of a binary tree is the number of edges between the two furthest nodes. For example, the diameter of the binary tree with the following structure: 
       1
      / \
     2   3
    / \     
   4   5    
is 3, which is the path between node 4 and node 5.

## Approach
To find the diameter of a binary tree, we will use a depth-first search (DFS) approach to calculate the height of each node. The diameter will be the maximum sum of the heights of the left and right subtrees of any node. We will keep track of the maximum diameter seen so far.

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
- The diameter of a binary tree can be calculated by finding the maximum sum of the heights of the left and right subtrees of any node.
- A DFS approach can be used to calculate the height of each node and keep track of the maximum diameter seen so far.
- The time complexity is O(N), where N is the number of nodes in the tree, and the space complexity is O(H), where H is the height of the tree.