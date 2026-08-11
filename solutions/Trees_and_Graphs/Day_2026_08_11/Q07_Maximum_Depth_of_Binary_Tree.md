# Maximum Depth of Binary Tree

## Problem Statement
Given a binary tree, find its maximum depth. The maximum depth of a binary tree is the number of nodes along the longest path from the root node down to the farthest leaf node. The path must start from the root and end at any leaf node. The depth of an empty tree is 0, and the depth of a tree with one node is 1. For example, the maximum depth of the binary tree `[3, 9, 20, null, null, 15, 7]` is 3, because the longest path from the root node to a leaf node is `3 -> 20 -> 7`.

## Approach
The algorithm uses a recursive approach to calculate the maximum depth of the binary tree. It checks if the tree is empty, and if so, returns 0. Otherwise, it recursively calculates the maximum depth of the left and right subtrees and returns the maximum of the two plus 1.

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
    int maxDepth(TreeNode* root) {
        // Base case: if the tree is empty, return 0
        if (root == nullptr) {
            return 0;
        }
        
        // Recursively calculate the maximum depth of the left and right subtrees
        int left_depth = maxDepth(root->left);
        int right_depth = maxDepth(root->right);
        
        // Return the maximum of the two depths plus 1
        return max(left_depth, right_depth) + 1;
    }
};
```

## Test Cases
```
Input: [3, 9, 20, null, null, 15, 7]
Output: 3
Input: [1, null, 2]
Output: 2
Input: []
Output: 0
```

## Key Takeaways
- The maximum depth of a binary tree can be calculated using a recursive approach.
- The time complexity of the solution is O(n), where n is the number of nodes in the tree.
- The space complexity of the solution is O(h), where h is the height of the tree.