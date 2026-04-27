# Binary Tree Maximum Path Sum

## Problem Statement
The problem requires finding the maximum path sum in a binary tree, where a path is defined as a sequence of nodes from any node to any other node in the tree. The path must go through at least one node, and the path can be a single node. The maximum path sum is the maximum sum of node values in any path in the tree. The input is the root of the binary tree, and the output is the maximum path sum. The tree nodes have values that can be positive or negative, and the path can start and end at any node.

## Approach
The algorithm uses a recursive depth-first search (DFS) to calculate the maximum path sum. For each node, it calculates the maximum path sum including the current node as the start and end of the path, and the maximum path sum including the current node as part of a larger path. The maximum path sum is updated at each node based on these calculations.

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
        
        // Update the maximum path sum if the current path sum is greater
        max_sum = max(max_sum, node->val + left_sum + right_sum);
        
        // Return the maximum path sum including the current node
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
- The maximum path sum can start and end at any node in the tree.
- The path can be a single node.
- The DFS approach allows for efficient calculation of the maximum path sum by considering all possible paths in the tree.
- The use of a reference variable `max_sum` allows for updating the maximum path sum at each node.