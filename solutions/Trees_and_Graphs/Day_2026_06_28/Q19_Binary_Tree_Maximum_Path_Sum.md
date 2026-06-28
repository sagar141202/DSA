# Binary Tree Maximum Path Sum

## Problem Statement
Given a binary tree, find the maximum path sum. The path sum is the sum of node values in a path from any node to any other node in the tree. The path must go through at least one node, and it can be a single node. The input tree is not guaranteed to be a binary search tree, and it can be empty. For example, given the binary tree `[-10,9,20,null,null,15,7]`, the maximum path sum is `42`, which is the sum of the node values in the path `20 -> 15 -> 7`.

## Approach
The algorithm uses a recursive depth-first search (DFS) to calculate the maximum path sum. It maintains a global maximum sum variable and updates it whenever a larger path sum is found. The DFS function returns the maximum path sum that includes the current node.

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
        if (node == nullptr) return 0;
        
        // Calculate the maximum path sum for the left and right subtrees
        int left_sum = max(dfs(node->left, max_sum), 0);
        int right_sum = max(dfs(node->right, max_sum), 0);
        
        // Update the maximum path sum if the current path sum is larger
        max_sum = max(max_sum, node->val + left_sum + right_sum);
        
        // Return the maximum path sum that includes the current node
        return node->val + max(left_sum, right_sum);
    }
};
```

## Test Cases
```
Input: [-10,9,20,null,null,15,7]
Output: 42
```

## Key Takeaways
- The problem can be solved using a recursive DFS approach.
- The DFS function returns the maximum path sum that includes the current node.
- The maximum path sum is updated whenever a larger path sum is found.