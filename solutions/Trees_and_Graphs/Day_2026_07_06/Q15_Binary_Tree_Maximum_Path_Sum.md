# Binary Tree Maximum Path Sum

## Problem Statement
Given a binary tree, find the maximum path sum. The path sum is the sum of the node values in a path from any node to any other node in the tree. The path must go through at least one node, and it can be a path that starts and ends at the same node. The input tree is non-empty and contains at most 1000 nodes. Each node's value is between -1000 and 1000.

## Approach
The approach to solve this problem is to use a recursive depth-first search (DFS) to calculate the maximum path sum for each node. We will consider two types of paths: paths that start and end at the current node, and paths that start at the current node but end at a different node.

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
        int left_sum = max(0, dfs(node->left, max_sum));
        int right_sum = max(0, dfs(node->right, max_sum));
        
        // Update the maximum path sum if the current path sum is greater
        max_sum = max(max_sum, node->val + left_sum + right_sum);
        
        // Return the maximum path sum that includes the current node
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
- The maximum path sum can be obtained by considering all possible paths in the tree.
- Using a recursive DFS approach can simplify the solution and avoid redundant calculations.
- The time complexity is O(N) because we visit each node once, and the space complexity is O(H) due to the recursive call stack.