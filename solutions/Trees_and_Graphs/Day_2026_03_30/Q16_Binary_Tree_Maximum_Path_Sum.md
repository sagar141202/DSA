# Binary Tree Maximum Path Sum

## Problem Statement
Given a binary tree, find the maximum path sum. The path must start and end at any node in the tree, and can go through any number of nodes. The path sum is the sum of the node values in the path. For example, given the binary tree `[-10,9,20,null,null,15,7]`, the maximum path sum is `42`, which is the sum of the nodes in the path `20 -> 15 -> 7`. The input tree is guaranteed to have at least one node.

## Approach
The algorithm uses a recursive depth-first search to calculate the maximum path sum. It keeps track of the maximum path sum found so far and updates it whenever a larger sum is found. The key insight is to consider each node as the starting point of the path and calculate the maximum path sum that includes the current node.

## Complexity
- Time: O(n)
- Space: O(h)

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
- The maximum path sum can be found by considering each node as the starting point of the path.
- The recursive depth-first search approach allows us to efficiently calculate the maximum path sum.
- The time complexity is O(n), where n is the number of nodes in the tree, since we visit each node once.