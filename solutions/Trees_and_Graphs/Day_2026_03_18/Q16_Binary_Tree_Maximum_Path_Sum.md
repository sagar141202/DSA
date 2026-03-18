# Binary Tree Maximum Path Sum

## Problem Statement
Given a binary tree, find the maximum path sum. The path must start and end at any node in the tree, and can go through any number of nodes. The path sum is the sum of the node values. The input tree is represented as a binary tree where each node has a value and two children (left and right). The tree can have negative values. For example, given the binary tree:
       -10
       / \
      9  20
         / \
        15  7
The maximum path sum is 42, which is the path 15 -> 20 -> 7.

## Approach
The algorithm uses a depth-first search (DFS) approach to calculate the maximum path sum. It recursively calculates the maximum path sum for each node and its subtrees, considering all possible paths. The maximum path sum is updated at each step.

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
        
        // Update the maximum path sum
        max_sum = max(max_sum, node->val + left_sum + right_sum);
        
        // Return the maximum path sum for the current node
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
- The algorithm uses a recursive DFS approach to calculate the maximum path sum.
- The maximum path sum is updated at each step by considering all possible paths.
- The time complexity is O(N), where N is the number of nodes in the tree.