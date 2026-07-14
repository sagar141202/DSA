# Binary Tree Maximum Path Sum

## Problem Statement
Given a binary tree, find the maximum path sum. The path sum is the sum of the node values in a path from any node to any other node in the tree. The path must go through at least one node, and it can't contain the same node more than once. For example, given the binary tree `-10(9, 20(15, 7))`, the maximum path sum is `20 + 15 + 7 = 42`.

## Approach
We use a depth-first search (DFS) approach to calculate the maximum path sum. The algorithm recursively calculates the maximum path sum of the left and right subtrees and updates the maximum path sum if the current path sum is greater.

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
    int maxPathSum(TreeNode* root) {
        int max_sum = INT_MIN;
        dfs(root, max_sum);
        return max_sum;
    }
    
    int dfs(TreeNode* node, int& max_sum) {
        if (!node) return 0;
        
        // Calculate the maximum path sum of the left and right subtrees
        int left_sum = max(dfs(node->left, max_sum), 0);
        int right_sum = max(dfs(node->right, max_sum), 0);
        
        // Update the maximum path sum if the current path sum is greater
        max_sum = max(max_sum, node->val + left_sum + right_sum);
        
        // Return the maximum path sum of the current node
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
- Use DFS to calculate the maximum path sum of the left and right subtrees.
- Update the maximum path sum if the current path sum is greater.
- Handle negative node values by taking the maximum of the current node value and 0.