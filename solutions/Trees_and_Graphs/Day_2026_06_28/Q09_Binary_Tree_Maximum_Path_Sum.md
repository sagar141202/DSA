# Binary Tree Maximum Path Sum

## Problem Statement
The problem is to find the maximum path sum in a binary tree, where a path is defined as a sequence of nodes from any node to any other node in the tree. The path must go through at least one node, and does not need to go through the root. Each node in the tree has a value, and the path sum is the sum of the values of all nodes in the path. The maximum path sum is the maximum sum of all possible paths in the tree. For example, given the binary tree:
```
     1
    / \
   2   3
```
The maximum path sum is 6 (2 + 1 + 3). If the tree is:
```
    -10
    / \
   9  20
     /  \
    15   7
```
The maximum path sum is 42 (15 + 20 + 7).

## Approach
The algorithm uses a depth-first search (DFS) to traverse the tree and calculate the maximum path sum. The DFS function returns the maximum path sum that includes the current node. The maximum path sum is updated if the current path sum is greater than the maximum path sum found so far.

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
Input: 
    -10
    / \
   9  20
     /  \
    15   7
Output: 42
```

## Key Takeaways
- The maximum path sum can be obtained by considering all possible paths in the tree.
- The DFS function returns the maximum path sum that includes the current node.
- The maximum path sum is updated if the current path sum is greater than the maximum path sum found so far.