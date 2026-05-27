# Path Sum

## Problem Statement
Given the root of a binary tree and an integer `targetSum`, return `true` if the tree has a root-to-leaf path such that adding up all the values along the path equals `targetSum`. A leaf is a node with no children. The path must start at the root and end at a leaf node. For example, given the binary tree `root = [5,4,8,11,null,13,4,7,2,null,null,5,1]` and `targetSum = 22`, the function should return `true` because the path `5 -> 4 -> 11 -> 2` sums up to 22.

## Approach
We will use a recursive depth-first search (DFS) approach to traverse the tree and check each root-to-leaf path. We'll keep track of the current sum of node values along the path and compare it with the target sum when we reach a leaf node.

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
    bool hasPathSum(TreeNode* root, int targetSum) {
        // Base case: if the tree is empty, return false
        if (!root) return false;
        
        // If the current node is a leaf node, check if its value equals the target sum
        if (!root->left && !root->right) return root->val == targetSum;
        
        // Recursively traverse the left and right subtrees, subtracting the current node's value from the target sum
        targetSum -= root->val;
        return hasPathSum(root->left, targetSum) || hasPathSum(root->right, targetSum);
    }
};
```

## Test Cases
```
Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: true
Input: root = [1,2,3], targetSum = 5
Output: false
```

## Key Takeaways
- Use recursive DFS to traverse the binary tree and check each root-to-leaf path.
- Keep track of the current sum of node values along the path and compare it with the target sum when reaching a leaf node.
- Base cases are essential in recursive solutions to handle edge cases and prevent infinite loops.