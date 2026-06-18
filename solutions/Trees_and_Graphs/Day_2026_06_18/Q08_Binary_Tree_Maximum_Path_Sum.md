# Binary Tree Maximum Path Sum

## Problem Statement
Given a binary tree, find the maximum path sum. The path must start and end at any node in the tree. The path can be any path from a node to any other node, and it can go through the root. The path sum is the sum of the node values in the path. For example, given the binary tree `[-10,9,20,null,null,15,7]`, the maximum path sum is `42`, which is the sum of the node values in the path `20 -> 15 -> 7`.

## Approach
The algorithm uses a recursive approach to calculate the maximum path sum. It calculates the maximum path sum for the left and right subtrees and combines them to find the maximum path sum for the current node. The maximum path sum is updated if the current path sum is greater than the maximum path sum found so far.

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
        
        // calculate the maximum gain for the left and right subtrees
        int left_gain = max(maxGain(node->left, max_sum), 0);
        int right_gain = max(maxGain(node->right, max_sum), 0);
        
        // update the maximum path sum if the current path sum is greater
        max_sum = max(max_sum, node->val + left_gain + right_gain);
        
        // return the maximum gain for the current node
        return node->val + max(left_gain, right_gain);
    }
};
```

## Test Cases
```
Input: [-10,9,20,null,null,15,7]
Output: 42
```

## Key Takeaways
- The maximum path sum can be any path from a node to any other node, and it can go through the root.
- The algorithm uses a recursive approach to calculate the maximum path sum.
- The time complexity is O(N), where N is the number of nodes in the tree, and the space complexity is O(H), where H is the height of the tree.