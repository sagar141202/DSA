# Binary Tree Maximum Path Sum

## Problem Statement
Given a binary tree, find the maximum path sum. The path sum is the sum of the node values in a path from any node to any other node in the tree. The path must go through at least one node, and it can be a path that starts and ends at the same node. The input tree is not guaranteed to be a binary search tree, and the node values can be positive or negative. The function should return the maximum path sum.

## Approach
The algorithm uses a recursive approach to calculate the maximum path sum by considering each node as the starting point of the path. It calculates the maximum path sum of the left and right subtrees and combines them to find the maximum path sum. The base case is when the tree is empty, in which case the maximum path sum is 0.

## Complexity
- Time: O(N)
- Space: O(H)

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
Input: [1,2,3]
Output: 6
Input: [-10,9,20,null,null,15,7]
Output: 42
```

## Key Takeaways
- The maximum path sum can be calculated by considering each node as the starting point of the path.
- The recursive approach can be used to calculate the maximum path sum by combining the maximum path sums of the left and right subtrees.
- The base case is when the tree is empty, in which case the maximum path sum is 0.