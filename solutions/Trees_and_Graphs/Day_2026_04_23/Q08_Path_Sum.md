# Path Sum

## Problem Statement
Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where each path's sum equals targetSum. A path is considered valid if there is a path from the root to a leaf node and the sum of all node values in the path equals the targetSum. The binary tree node has a value and two children, left and right. The problem requires finding all such paths in the tree.

## Approach
The algorithm uses a recursive depth-first search (DFS) approach to traverse the binary tree, maintaining the current path and its sum. When a leaf node is reached, the current path's sum is compared to the targetSum. If they match, the path is added to the result list. The DFS traversal ensures all possible paths are explored.

## Complexity
- Time: O(N^2) in the worst case, where N is the number of nodes, due to the path construction in each recursive call.
- Space: O(N) for the recursion stack and the space needed to store the paths.

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
        
        // Add current node's value to the path and subtract from targetSum
        path.push_back(node->val);
        targetSum -= node->val;
        
        // If the node is a leaf and targetSum is 0, add the path to the result
        if (node->left == nullptr && node->right == nullptr && targetSum == 0) {
            result.push_back(path);
        } else {
            // Recursively explore the left and right subtrees
            dfs(node->left, targetSum, path, result);
            dfs(node->right, targetSum, path, result);
        }
        
        // Backtrack by removing the current node's value from the path
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
- Use recursive DFS to explore all paths in the binary tree.
- Maintain the current path and its sum during the DFS traversal.
- Backtrack by removing the current node's value from the path after exploring its subtrees.