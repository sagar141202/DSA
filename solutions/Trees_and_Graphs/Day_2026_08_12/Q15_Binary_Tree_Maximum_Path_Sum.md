# Binary Tree Maximum Path Sum

## Problem Statement
Given a binary tree, find the maximum path sum. The path must start and end at any node in the tree, and it can only go through nodes that have a parent-child relationship. The path can be from a node to any of its descendants, or from any node to the root. The path sum is the sum of all node values in the path. For example, given the binary tree `[-10,9,20,null,null,15,7]`, the maximum path sum is `42` which is from node `20` to node `15` to node `7`.

## Approach
The algorithm uses a depth-first search (DFS) approach to calculate the maximum path sum. It recursively calculates the maximum path sum for each node and updates the maximum path sum if a larger sum is found. The key insight is to consider the maximum path sum that includes the current node and its subtrees.

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
        int left = max(dfs(node->left, max_sum), 0);
        int right = max(dfs(node->right, max_sum), 0);
        max_sum = max(max_sum, node->val + left + right);
        return node->val + max(left, right);
    }
};
```

## Test Cases
```
Input: [-10,9,20,null,null,15,7]
Output: 42
```

## Key Takeaways
- Use DFS to recursively calculate the maximum path sum for each node.
- Keep track of the maximum path sum found so far.
- Consider the maximum path sum that includes the current node and its subtrees.