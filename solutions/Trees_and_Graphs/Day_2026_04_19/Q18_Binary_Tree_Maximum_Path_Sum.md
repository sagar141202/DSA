# Binary Tree Maximum Path Sum

## Problem Statement
Given a binary tree, find the maximum path sum. The path sum is defined as the sum of the node values in a path from any node to any other node in the tree. The path can be from a node to its descendant, or from a node to its ancestor, or between two nodes in different subtrees. The maximum path sum is the maximum sum of node values in any path in the tree. For example, in the binary tree with the following structure:
       1
      / \
     2   3
the maximum path sum is 6 (2 + 1 + 3).

## Approach
The algorithm uses a recursive Depth-First Search (DFS) approach to calculate the maximum path sum. It maintains a global maximum sum and updates it whenever a larger path sum is found. The DFS function calculates the maximum path sum for each node by considering the maximum path sum of its left and right subtrees.

## Complexity
- Time: O(N)
- Space: O(H)

## C++ Solution
```cpp
#include <iostream>
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
        
        // Update the maximum path sum if a larger path sum is found
        max_sum = max(max_sum, node->val + left_sum + right_sum);
        
        // Return the maximum path sum for the current node
        return node->val + max(left_sum, right_sum);
    }
};
```

## Test Cases
```
Input: [1,2,3]
Output: 6
Input: [-10,9,20,null,null,15,7]
Output: 42
```

## Key Takeaways
- The maximum path sum can be found by considering all possible paths in the binary tree.
- The DFS approach is suitable for solving this problem due to its ability to traverse the tree and calculate the maximum path sum for each node.
- The use of a global variable to store the maximum path sum allows for efficient updates and returns the final result.