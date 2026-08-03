# Path Sum

## Problem Statement
Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where each path's sum equals targetSum. A leaf is a node with no children. The path sum is the sum of all node values in the path. The tree has the following structure: each node has a value, and two children (left and right). The function should return all paths where the sum of node values equals the targetSum.

## Approach
The approach to solve this problem is to use a Depth-First Search (DFS) algorithm with recursion to traverse the binary tree. We will maintain a running sum of node values and check if the current node is a leaf node. If the current node is a leaf node and the running sum equals the targetSum, we add the current path to the result.

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
        
        // Add current node to the path
        path.push_back(node->val);
        targetSum -= node->val;
        
        // If current node is a leaf node and targetSum equals 0, add the current path to the result
        if (!node->left && !node->right && targetSum == 0) {
            result.push_back(path);
        }
        
        // Recursively traverse the left and right subtrees
        dfs(node->left, targetSum, path, result);
        dfs(node->right, targetSum, path, result);
        
        // Remove the current node from the path (backtracking)
        path.pop_back();
    }
};
```

## Test Cases
```
Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: [[5,4,11,2],[5,8,4,5]]
```

## Key Takeaways
- Use DFS with recursion to traverse the binary tree.
- Maintain a running sum of node values and check if the current node is a leaf node.
- Use backtracking to remove the current node from the path after exploring its subtrees.