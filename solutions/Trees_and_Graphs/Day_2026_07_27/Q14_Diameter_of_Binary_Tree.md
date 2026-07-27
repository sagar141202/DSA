# Diameter of Binary Tree

## Problem Statement
The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root. Given a binary tree, find the length of the diameter of the tree. The diameter of a tree is the number of edges in the longest path between two nodes. The function should return the diameter of the binary tree. For example, given a binary tree with the following structure: 
       1
      / \
     2   3
    / \     
   4   5    
The diameter of this tree is 3, which is the path between node 4 and node 5.

## Approach
To find the diameter, we will use a depth-first search (DFS) approach to calculate the height of each node. The diameter will be the maximum sum of the heights of the left and right subtrees. We will keep track of the maximum diameter found so far.

## Complexity
- Time: O(N)
- Space: O(H), where N is the number of nodes and H is the height of the tree

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
        int maxDiameter = 0;
        dfs(root, maxDiameter);
        return maxDiameter;
    }
    
    int dfs(TreeNode* node, int& maxDiameter) {
        if (!node) return 0;
        
        int leftHeight = dfs(node->left, maxDiameter);
        int rightHeight = dfs(node->right, maxDiameter);
        
        maxDiameter = max(maxDiameter, leftHeight + rightHeight);
        
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
      / \
     2   3
    / \
   4   5
  / \
 6   7
Output: 4
```

## Key Takeaways
- The diameter of a binary tree can be calculated using DFS to find the height of each node.
- The diameter is the maximum sum of the heights of the left and right subtrees.
- The time complexity is O(N), where N is the number of nodes in the tree.