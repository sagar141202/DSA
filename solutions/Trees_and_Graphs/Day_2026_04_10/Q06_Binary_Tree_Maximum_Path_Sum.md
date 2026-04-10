# Binary Tree Maximum Path Sum

## Problem Statement
Given a binary tree, find the maximum path sum. The path must start and end at any node in the tree, and the path can only be composed of parent-child pairs. The path sum is the sum of the node values in the path. For example, given the binary tree `[-10,9,20,null,null,15,7]`, the maximum path sum is `42` which is the sum of the node values in the path `20 -> 15 -> 7`. The tree node has the following definition: `struct TreeNode { int val; TreeNode *left; TreeNode *right; TreeNode() : val(0), left(nullptr), right(nullptr) {}; TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}; TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {} };`.

## Approach
The algorithm uses a recursive depth-first search (DFS) to traverse the tree, calculating the maximum path sum at each node. The DFS function returns the maximum path sum that includes the current node and one of its child nodes. The maximum path sum is updated at each node if a larger path sum is found.

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
        int left_sum = max(dfs(node->left, max_sum), 0);
        int right_sum = max(dfs(node->right, max_sum), 0);
        
        // Update the maximum path sum if a larger path sum is found
        max_sum = max(max_sum, node->val + left_sum + right_sum);
        
        // Return the maximum path sum that includes the current node and one of its child nodes
        return node->val + max(left_sum, right_sum);
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
- Use a recursive DFS to traverse the tree and calculate the maximum path sum at each node.
- Update the maximum path sum at each node if a larger path sum is found.
- The DFS function returns the maximum path sum that includes the current node and one of its child nodes.