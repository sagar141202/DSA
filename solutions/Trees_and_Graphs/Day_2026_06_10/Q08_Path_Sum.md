# Path Sum

## Problem Statement
Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals the targetSum. The path must go from the root to a leaf node, and all node values in the path must be included in the sum. The binary tree has the following structure: each node has a value and two children (left child and right child). The root of the binary tree is given, and the integer targetSum is also given. For example, given the binary tree with root [5,4,8,11,null,13,4,7,2,null,null,5,1] and targetSum 22, the output should be [[5,4,11,2], [5,8,4,5]].

## Approach
The algorithm uses a depth-first search (DFS) approach to traverse the binary tree and find all root-to-leaf paths where the sum of the node values equals the targetSum. The DFS function is recursive and keeps track of the current path and its sum. When a leaf node is reached, the function checks if the current sum equals the targetSum and adds the path to the result if it does.

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
    vector<vector<int>> pathSum(TreeNode* root, int targetSum) {
        vector<vector<int>> result;
        vector<int> path;
        dfs(root, targetSum, path, result);
        return result;
    }
    
    void dfs(TreeNode* node, int targetSum, vector<int>& path, vector<vector<int>>& result) {
        if (!node) return;
        path.push_back(node->val);
        targetSum -= node->val;
        if (!node->left && !node->right && targetSum == 0) {
            result.push_back(path);
        }
        dfs(node->left, targetSum, path, result);
        dfs(node->right, targetSum, path, result);
        path.pop_back();
    }
};
```

## Test Cases
```
Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: [[5,4,11,2], [5,8,4,5]]
Input: root = [1,2,3], targetSum = 5
Output: []
Input: root = [0], targetSum = 0
Output: [[0]]
```

## Key Takeaways
- Use DFS to traverse the binary tree and find all root-to-leaf paths where the sum of the node values equals the targetSum.
- Keep track of the current path and its sum using a recursive DFS function.
- When a leaf node is reached, check if the current sum equals the targetSum and add the path to the result if it does.