# Path Sum

## Problem Statement
Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values equals the targetSum. The path must start at the root and end at a leaf node, and all node values in the path must be added to get the targetSum. The binary tree has the following structure: each node has a unique value, and each node has at most two children (i.e., left child and right child). The input is guaranteed to be a non-empty binary tree, and the targetSum is a 32-bit signed integer. For example, given the binary tree with the following structure:
       5
      / \
     4   8
    /   / \
   11  13  4
  / \       \
 7   2       5
and targetSum = 22, the output should be [[5,4,11,2], [5,8,4,5]].

## Approach
The solution uses a depth-first search (DFS) approach to traverse the binary tree, keeping track of the current path and its sum. When a leaf node is reached, the current path is added to the result if its sum equals the targetSum. The DFS function is recursive, allowing it to efficiently explore all possible paths in the tree.

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
        vector<int> currentPath;
        dfs(root, targetSum, currentPath, result);
        return result;
    }
    
    void dfs(TreeNode* node, int remainingSum, vector<int>& currentPath, vector<vector<int>>& result) {
        if (!node) return;
        
        currentPath.push_back(node->val);
        remainingSum -= node->val;
        
        if (!node->left && !node->right && remainingSum == 0) {
            result.push_back(currentPath);
        } else {
            dfs(node->left, remainingSum, currentPath, result);
            dfs(node->right, remainingSum, currentPath, result);
        }
        
        currentPath.pop_back();
    }
};
```

## Test Cases
```
Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: [[5,4,11,2],[5,8,4,5]]
```

## Key Takeaways
- Use DFS to traverse the binary tree and keep track of the current path and its sum.
- When a leaf node is reached, check if the current path sum equals the targetSum and add it to the result if true.
- Use recursion to efficiently explore all possible paths in the tree.