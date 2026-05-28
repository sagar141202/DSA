# Binary Tree Maximum Path Sum

## Problem Statement
Given a binary tree, find the maximum path sum. The path sum is the sum of node values in a path from any node to any other node in the tree. The path must go through at least one node, and does not need to go through the root. The maximum path sum is the maximum sum of node values in any path in the tree. For example, given the binary tree `[-10,9,20,null,null,15,7]`, the maximum path sum is `20 + 15 + 7 = 42`.

## Approach
The algorithm uses a recursive depth-first search (DFS) approach to traverse the tree, keeping track of the maximum path sum at each node. The maximum path sum is updated whenever a path with a larger sum is found. The DFS function returns the maximum path sum that includes the current node.

## Complexity
- Time: O(N), where N is the number of nodes in the tree
- Space: O(H), where H is the height of the tree

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
        maxPathSumHelper(root, max_sum);
        return max_sum;
    }
    
    int maxPathSumHelper(TreeNode* node, int& max_sum) {
        if (node == NULL) return 0;
        
        // Recursively calculate the maximum path sum for the left and right subtrees
        int left_sum = max(0, maxPathSumHelper(node->left, max_sum));
        int right_sum = max(0, maxPathSumHelper(node->right, max_sum));
        
        // Update the maximum path sum if the current path has a larger sum
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
- The maximum path sum can be negative if all node values are negative.
- The path must go through at least one node, but does not need to go through the root.
- The recursive DFS approach allows for efficient calculation of the maximum path sum.