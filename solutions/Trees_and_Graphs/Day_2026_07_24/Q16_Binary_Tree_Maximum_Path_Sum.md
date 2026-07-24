# Binary Tree Maximum Path Sum

## Problem Statement
The problem requires finding the maximum path sum in a binary tree, where a path can be defined as a sequence of nodes from any node to any other node in the tree. The path must consist of at least one node, and the path can go through any node in the tree. The maximum path sum is the maximum sum of node values along any path in the tree. The input is the root of the binary tree, and the output is the maximum path sum. For example, given the binary tree:
```
     1
    / \
   2   3
```
The maximum path sum is 6 (1 + 2 + 3).

## Approach
The algorithm uses a recursive approach to calculate the maximum path sum. It calculates the maximum path sum for the left and right subtrees and then combines them to find the maximum path sum for the current node. The intuition is to consider all possible paths that pass through each node and keep track of the maximum sum found so far.

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
        
        // Calculate the maximum gain for the left and right subtrees
        int left_gain = max(maxGain(node->left, max_sum), 0);
        int right_gain = max(maxGain(node->right, max_sum), 0);
        
        // Update the maximum sum if the current path sum is greater
        max_sum = max(max_sum, node->val + left_gain + right_gain);
        
        // Return the maximum gain for the current node
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
- The maximum path sum can be obtained by considering all possible paths that pass through each node.
- The recursive approach allows us to calculate the maximum path sum for each node and keep track of the maximum sum found so far.
- The time complexity is O(N), where N is the number of nodes in the tree, since we visit each node once. The space complexity is O(H), where H is the height of the tree, due to the recursive call stack.