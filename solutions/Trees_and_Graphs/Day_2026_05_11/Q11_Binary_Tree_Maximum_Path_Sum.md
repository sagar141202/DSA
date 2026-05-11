# Binary Tree Maximum Path Sum

## Problem Statement
The problem requires finding the maximum path sum in a binary tree, where a path is defined as a sequence of nodes from any node to any other node in the tree. The path must go through at least one node, and the path can start and end at any node. The maximum path sum is the maximum sum of node values in any path in the tree. The tree is not guaranteed to be a binary search tree, and the node values can be positive or negative. For example, given the binary tree `[-10,9,20,null,null,15,7]`, the maximum path sum is `42` (from node `20` to node `15` to node `7`).

## Approach
The algorithm uses a recursive depth-first search approach to calculate the maximum path sum of each subtree. It keeps track of the maximum path sum seen so far and updates it whenever a path with a larger sum is found. The key insight is to consider each node as the starting point of a path and calculate the maximum path sum that includes this node.

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
        maxGain(root, max_sum);
        return max_sum;
    }
    
    int maxGain(TreeNode* node, int& max_sum) {
        if (!node) return 0;
        
        // Calculate the maximum gain for the left and right subtrees
        int left_gain = max(maxGain(node->left, max_sum), 0);
        int right_gain = max(maxGain(node->right, max_sum), 0);
        
        // Update the maximum path sum if the current path has a larger sum
        max_sum = max(max_sum, node->val + left_gain + right_gain);
        
        // Return the maximum gain for the current node
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
- The maximum path sum can start and end at any node in the tree.
- The recursive depth-first search approach allows us to efficiently calculate the maximum path sum for each subtree.
- Keeping track of the maximum path sum seen so far enables us to update the result whenever a path with a larger sum is found.