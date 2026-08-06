# Binary Tree Maximum Path Sum

## Problem Statement
Given a binary tree, find the maximum path sum. The path must start and end at any node in the tree, and the path can only go through nodes and edges in the tree. The path can be composed of multiple nodes, and the sum of the node values is the path sum. For example, given the binary tree `[-10,9,20,null,null,15,7]`, the maximum path sum is `42`, which is the sum of the node values in the path `20 -> 15 -> 7`. The input tree is guaranteed to have at least one node and at most 1000 nodes, and the node values are integers in the range `[-1000, 1000]`.

## Approach
The algorithm uses a recursive depth-first search to calculate the maximum path sum. It maintains a global maximum path sum and updates it whenever a larger path sum is found. The function recursively calculates the maximum path sum for the left and right subtrees and returns the maximum path sum that includes the current node.

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
Input: [1,2,3]
Output: 6
```

## Key Takeaways
- The maximum path sum can start and end at any node in the tree.
- The path can only go through nodes and edges in the tree.
- The recursive depth-first search approach can be used to calculate the maximum path sum efficiently.