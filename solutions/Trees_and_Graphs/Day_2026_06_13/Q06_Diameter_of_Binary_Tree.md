# Diameter of Binary Tree

## Problem Statement
Given a binary tree, find the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root. The length of a path between two nodes is represented by the number of edges between them. For example, the diameter of the binary tree with the following nodes: 
       1
      / \
     2   3
    / \
   4   5
is 3, which is the path between node 4 and node 5. The input tree is guaranteed to be non-empty.

## Approach
We can solve this problem by calculating the height of the left and right subtrees for each node and keeping track of the maximum diameter found so far. The diameter of a tree is the maximum diameter of its subtrees or the sum of the heights of its left and right subtrees.

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
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
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
- To calculate the diameter of a binary tree, we need to consider the diameter of its subtrees and the sum of the heights of its left and right subtrees.
- The time complexity is O(N) because we visit each node once.
- The space complexity is O(H) due to the recursive call stack, where H is the height of the tree.