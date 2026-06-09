# Binary Tree Maximum Path Sum

## Problem Statement
The problem requires finding the maximum path sum in a binary tree, where the path sum is defined as the sum of node values in a path from any node to any other node in the tree. The path can be from a parent to a child or vice versa. The input is the root of the binary tree, and the output is the maximum path sum. The tree nodes have integer values, and the path sum can be negative.

## Approach
The algorithm uses a recursive depth-first search (DFS) approach to traverse the tree and calculate the maximum path sum. It maintains a variable to store the maximum path sum found so far. For each node, it calculates the maximum path sum including the current node and updates the maximum path sum if necessary.

## Complexity
- Time: O(N), where N is the number of nodes in the tree, since each node is visited once.
- Space: O(H), where H is the height of the tree, due to the recursive call stack.

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
        
        // Update the maximum path sum if the current path sum is greater
        max_sum = max(max_sum, node->val + left_sum + right_sum);
        
        // Return the maximum path sum including the current node
        return node->val + max(left_sum, right_sum);
    }
};
```

## Test Cases
```
Input: root = [1,2,3]
Output: 6
Explanation: The maximum path sum is 1 + 2 + 3 = 6.

Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The maximum path sum is 20 + 15 + 7 = 42.
```

## Key Takeaways
- The maximum path sum can be negative if all node values are negative.
- The algorithm uses a recursive DFS approach to traverse the tree and calculate the maximum path sum.
- The time complexity is O(N), where N is the number of nodes in the tree, and the space complexity is O(H), where H is the height of the tree.