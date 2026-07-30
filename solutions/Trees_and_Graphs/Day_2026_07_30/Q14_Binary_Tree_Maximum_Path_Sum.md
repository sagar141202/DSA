# Binary Tree Maximum Path Sum

## Problem Statement
Given a binary tree, find the maximum path sum. The path sum is the sum of node values in a path from any node to any other node in the tree. The path can be from a node to its descendant, or from a node to its ancestor, or between two nodes that are not necessarily connected by an edge. Each node has a value, and the maximum path sum is the maximum sum of the node values in any path. For example, given the binary tree:
```
     1
    / \
   2   3
```
The maximum path sum is 6 (1 + 2 + 3). 

## Approach
The algorithm uses a recursive depth-first search (DFS) to calculate the maximum path sum for each subtree. It keeps track of the maximum path sum seen so far and updates it whenever a larger sum is found. The base case is when the tree is empty, in which case the maximum path sum is 0.

## Complexity
- Time: O(N)
- Space: O(H)

## C++ Solution
```cpp
#include <iostream>
using namespace std;

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
        
        int left_sum = max(0, dfs(node->left, max_sum));
        int right_sum = max(0, dfs(node->right, max_sum));
        
        max_sum = max(max_sum, node->val + left_sum + right_sum);
        
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
- Use DFS to traverse the tree and calculate the maximum path sum for each subtree.
- Keep track of the maximum path sum seen so far and update it whenever a larger sum is found.
- Handle the case when a node's value is negative by setting its contribution to 0.