# Path Sum

## Problem Statement
Given a binary tree and a target sum, find all root-to-leaf paths where the sum of the node values equals the target sum. The binary tree node has an integer value and at most two children (i.e., left child and right child). The path sum is calculated by summing up all node values from the root to a leaf node. For example, given a binary tree with the following structure:
       5
      / \
     4   8
    /   / \
   11  13  4
  / \      / \
 7   2    5   1
The target sum is 22. The paths that sum up to the target are [5,4,11,2] and [5,8,4,5].

## Approach
The approach to solve this problem is to use a depth-first search (DFS) algorithm to traverse the binary tree and keep track of the current path sum. We will recursively call the DFS function for the left and right child nodes and update the path sum accordingly.

## Complexity
- Time: O(N)
- Space: O(H), where N is the number of nodes in the binary tree and H is the height of the binary tree.

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
    vector<vector<int>> pathSum(TreeNode* root, int sum) {
        vector<vector<int>> result;
        vector<int> path;
        dfs(root, sum, path, result);
        return result;
    }
    
    void dfs(TreeNode* node, int sum, vector<int>& path, vector<vector<int>>& result) {
        if (!node) return;
        path.push_back(node->val);
        sum -= node->val;
        if (!node->left && !node->right && sum == 0) {
            result.push_back(path);
        }
        dfs(node->left, sum, path, result);
        dfs(node->right, sum, path, result);
        path.pop_back();
    }
};
```

## Test Cases
```
Input: 
       5
      / \
     4   8
    /   / \
   11  13  4
  / \      / \
 7   2    5   1
Target Sum: 22
Output: [[5,4,11,2], [5,8,4,5]]
```

## Key Takeaways
- Use DFS to traverse the binary tree and keep track of the current path sum.
- Recursively call the DFS function for the left and right child nodes and update the path sum accordingly.
- When a leaf node is reached and the path sum equals the target sum, add the path to the result.