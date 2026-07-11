# Path Sum

## Problem Statement
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum. A leaf is a node with no children. The path must start at the root and end at a leaf. For example, given the binary tree with root [5,4,8,11,null,13,4,7,2,null,null,5,1] and target sum 22, the function should return true because there exists a path 5 -> 4 -> 11 -> 2 which sums to 22.

## Approach
The algorithm uses a Depth-First Search (DFS) approach to traverse the tree, keeping track of the current sum of node values. If a leaf node is reached and its sum equals the target sum, the function returns true. The search continues until all paths have been explored.

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
        targetSum -= root->val; // subtract current node's value
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
- Use DFS to explore all possible paths in the tree.
- Keep track of the current sum of node values to determine if a path sum equals the target sum.
- Base cases include an empty tree and a leaf node, where the function returns false and checks the sum, respectively.