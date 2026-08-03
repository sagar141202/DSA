# Binary Tree Maximum Path Sum

## Problem Statement
Given a binary tree, find the maximum path sum. The path sum is the sum of the node values in a path from any node to any other node in the tree. This path can be a single node, or it can be a path that goes from one node, down through one child, and then back up to another node. The path must go through at least one node, and does not need to go through the root. For example, in the tree with nodes [1,2,3], the maximum path sum is 6, which is the sum of the nodes in the path from node 2 to node 3.

## Approach
The algorithm uses a depth-first search (DFS) approach to traverse the tree and calculate the maximum path sum. It maintains a variable to store the maximum path sum found so far. For each node, it calculates the maximum path sum that includes the current node and its children.

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
- The maximum path sum can be negative if all node values are negative.
- The path sum can include a single node, or it can include multiple nodes.
- The DFS approach allows us to efficiently traverse the tree and calculate the maximum path sum.