# Binary Tree Maximum Path Sum

## Problem Statement
Given a binary tree, find the maximum path sum. The path sum is the sum of the node values in a path from any node to any other node in the tree. The path must go through at least one node, and does not need to go through the root. For example, in the tree with nodes 1, 2, and 3, where node 1 has a left child node 2 and a right child node 3, the maximum path sum is 6 (1 + 2 + 3). The input will be the root of the binary tree, and the output should be the maximum path sum. The tree nodes will have values between -100 and 100, and the number of nodes in the tree will be between 1 and 1000.

## Approach
The algorithm will use a recursive depth-first search (DFS) approach to calculate the maximum path sum. It will keep track of the maximum path sum found so far and update it whenever a larger path sum is found. The DFS function will return the maximum path sum that includes the current node.

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
- The maximum path sum can be found using a recursive DFS approach.
- The DFS function should return the maximum path sum that includes the current node.
- The maximum path sum should be updated whenever a larger path sum is found.