# Binary Tree Maximum Path Sum

## Problem Statement
The problem requires finding the maximum path sum in a binary tree, where a path is defined as a sequence of nodes from any node to any other node in the tree. The path must go through at least one node, and it can be a single node. The maximum path sum is the maximum sum of node values in any path in the tree. The input is the root of the binary tree, and the output is the maximum path sum. For example, given the binary tree with nodes having values -10, 9, 20, 15, 7, the maximum path sum is 42, which is the sum of the node values in the path 20 -> 15 -> 7.

## Approach
The algorithm uses a recursive depth-first search (DFS) approach to calculate the maximum path sum. It keeps track of the maximum path sum found so far and updates it whenever a greater path sum is found. The DFS function calculates the maximum path sum for each subtree and returns the maximum path sum that includes the current node.

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
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    int maxPathSum(TreeNode* root) {
        int max_sum = INT_MIN;
        dfs(root, max_sum);
        return max_sum;
    }
    
    int dfs(TreeNode* node, int& max_sum) {
        if (!node) return 0;
        
        // Calculate the maximum path sum for the left and right subtrees
        int left_sum = max(0, dfs(node->left, max_sum));
        int right_sum = max(0, dfs(node->right, max_sum));
        
        // Update the maximum path sum if the current path sum is greater
        max_sum = max(max_sum, node->val + left_sum + right_sum);
        
        // Return the maximum path sum that includes the current node
        return node->val + max(left_sum, right_sum);
    }
};
```

## Test Cases
```
Input: root = [-10,9,20,null,null,15,7]
Output: 42
```

## Key Takeaways
- The maximum path sum can be negative if all node values are negative.
- The path can start and end at any node, not just the root.
- The recursive DFS approach allows for efficient calculation of the maximum path sum.