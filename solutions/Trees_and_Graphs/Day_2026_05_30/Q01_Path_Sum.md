# Path Sum

## Problem Statement
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum. A leaf is a node with no children. The path must start at the root and end at a leaf node. For example, given the binary tree:
```
    5
   / \
  4   8
 /   / \
11  13  4
/ \      \
7   2      1
```
and targetSum = 22, the function should return true because the path 5 -> 4 -> 11 -> 2 sums up to 22.

## Approach
The solution involves using a depth-first search (DFS) approach to traverse the binary tree, keeping track of the current sum of node values. If a leaf node is reached and the current sum equals the target sum, return true. The function will recursively explore all possible paths.

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
        if (!root) return false; // base case: empty tree
        if (!root->left && !root->right) { // leaf node
            return root->val == targetSum;
        }
        targetSum -= root->val; // subtract current node value
        return hasPathSum(root->left, targetSum) || hasPathSum(root->right, targetSum);
    }
};
```

## Test Cases
```
Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
```

## Key Takeaways
- Use DFS to traverse the binary tree and keep track of the current sum.
- Base case: if the tree is empty, return false.
- If a leaf node is reached, check if the current sum equals the target sum.