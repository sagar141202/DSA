# Binary Tree Maximum Path Sum

## Problem Statement
Given a binary tree, find the maximum path sum. The path must start and end at any node in the tree, and the path can only go through nodes in the tree. The path sum is the sum of the node values in the path. The input tree is a binary tree where each node has a value and two children (left and right). The tree can be empty, and the values in the tree can be positive, negative, or zero. For example, given the binary tree `[-10,9,20,null,null,15,7]`, the maximum path sum is `42` which is from node `20` to node `15` to node `7`.

## Approach
The approach is to use a recursive depth-first search (DFS) to traverse the tree and calculate the maximum path sum at each node. The maximum path sum at a node is the maximum of the current node's value, the sum of the current node's value and the maximum path sum of the left subtree, and the sum of the current node's value and the maximum path sum of the right subtree.

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
        int maxSum = INT_MIN;
        dfs(root, maxSum);
        return maxSum;
    }
    
    int dfs(TreeNode* node, int& maxSum) {
        if (!node) return 0;
        int left = max(0, dfs(node->left, maxSum));
        int right = max(0, dfs(node->right, maxSum));
        maxSum = max(maxSum, node->val + left + right);
        return node->val + max(left, right);
    }
};
```

## Test Cases
```
Input: [-10,9,20,null,null,15,7]
Output: 42
Input: [1,2,3]
Output: 6
```

## Key Takeaways
- The maximum path sum can start and end at any node in the tree.
- The path sum can only go through nodes in the tree.
- The recursive DFS approach can be used to calculate the maximum path sum at each node.