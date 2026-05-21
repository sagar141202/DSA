# Path Sum

## Problem Statement
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum. A leaf is a node with no children. The path must start at the root and end at a leaf node. For example, given the binary tree with root [5,4,8,11,null,13,4,7,2,null,null,5,1] and targetSum = 22, the function should return true because there is a path 5 -> 4 -> 11 -> 2 that sums up to 22.

## Approach
The approach to solve this problem is to use a recursive Depth-First Search (DFS) algorithm, traversing the tree and keeping track of the current sum of node values. If the current sum equals the target sum at a leaf node, the function returns true.

## Complexity
- Time: O(n)
- Space: O(h)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

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
        if (!root) return false;
        if (!root->left && !root->right) return root->val == targetSum;
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
- Use recursive DFS to traverse the tree and keep track of the current sum.
- Check if the current sum equals the target sum at a leaf node.
- The time complexity is O(n) where n is the number of nodes in the tree, and the space complexity is O(h) where h is the height of the tree.