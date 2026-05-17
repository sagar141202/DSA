# Binary Tree Maximum Path Sum

## Problem Statement
Given a binary tree, find the maximum path sum. The path must start and end at any node in the tree. The path can be any sequence of nodes from start to end, and each node can only be used once. The path can go through any number of nodes, including none (in which case the path sum is 0). The maximum path sum is the maximum sum of the node values along any path in the tree. For example, given the binary tree:
       -10
       / \
      9  20
         /  \
        15   7
The maximum path sum is 42, which is the sum of the node values along the path 15 -> 20 -> 7.

## Approach
The algorithm uses a recursive approach to calculate the maximum path sum. It calculates the maximum path sum of the left and right subtrees and then combines them to find the maximum path sum. The key idea is to keep track of the maximum path sum that includes the current node.

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
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    int maxPathSum(TreeNode* root) {
        int max_sum = INT_MIN;
        maxGain(root, max_sum);
        return max_sum;
    }
    
    int maxGain(TreeNode* node, int& max_sum) {
        if (!node) return 0;
        
        // Calculate the maximum gain of the left and right subtrees
        int left_gain = max(maxGain(node->left, max_sum), 0);
        int right_gain = max(maxGain(node->right, max_sum), 0);
        
        // Update the maximum path sum if the current path sum is greater
        max_sum = max(max_sum, node->val + left_gain + right_gain);
        
        // Return the maximum gain of the current node
        return node->val + max(left_gain, right_gain);
    }
};
```

## Test Cases
```
Input: root = [-10,9,20,null,null,15,7]
Output: 42
Input: root = [1,2,3]
Output: 6
```

## Key Takeaways
- The maximum path sum can be obtained by considering all possible paths in the tree.
- The recursive approach helps to calculate the maximum path sum by breaking down the problem into smaller sub-problems.
- The time complexity is O(N) because each node is visited once, and the space complexity is O(H) because of the recursive call stack.