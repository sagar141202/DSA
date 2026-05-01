# Binary Tree Maximum Path Sum

## Problem Statement
Given a binary tree, find the maximum path sum. The path must start and end at any node in the tree, and the path can only go through nodes in a parent-child relationship. The path can be thought of as a sequence of nodes, and the sum of the node values in this sequence is the path sum. The maximum path sum is the maximum sum of all possible paths in the tree. For example, given the binary tree `[-10,9,20,null,null,15,7]`, the maximum path sum is `42`, which is the sum of the nodes in the path `20 -> 15 -> 7`. The input tree will have at most `100` nodes, and each node's value will be between `-100` and `100`.

## Approach
The algorithm uses a recursive approach with depth-first search to calculate the maximum path sum. It keeps track of the maximum path sum found so far and updates it whenever a larger sum is found. The key insight is to consider each node as the starting point of a potential maximum path and explore all possible paths from that node.

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
    int maxPathSum(TreeNode* root) {
        int max_sum = INT_MIN;
        dfs(root, max_sum);
        return max_sum;
    }

    int dfs(TreeNode* node, int& max_sum) {
        if (!node) return 0;
        int left = max(dfs(node->left, max_sum), 0);
        int right = max(dfs(node->right, max_sum), 0);
        max_sum = max(max_sum, left + right + node->val);
        return max(left, right) + node->val;
    }
};
```

## Test Cases
```
Input: [-10,9,20,null,null,15,7]
Output: 42
```

## Key Takeaways
- The recursive approach allows for efficient exploration of all possible paths in the tree.
- Keeping track of the maximum path sum found so far enables the algorithm to return the correct result.
- Using a reference to the maximum sum variable (`int& max_sum`) allows the recursive function to update the maximum sum found so far.