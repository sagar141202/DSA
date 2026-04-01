# Path Sum

## Problem Statement
Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where each path's sum equals targetSum. A leaf is a node with no children. The path sum is the sum of all node values in the path. The tree has the following properties: The number of nodes in the tree is in the range [1, 100]. The values of the nodes in the tree are in the range [-100, 100]. The absolute value of targetSum is less than 1000. For example, given the binary tree with root [5,4,8,11,null,13,4,7,2,null,null,5,1] and target sum 22, return [[5,4,11,2],[5,8,4,5]].

## Approach
The solution uses a depth-first search (DFS) approach to traverse the binary tree, keeping track of the current path sum and storing paths that sum up to the target value. The algorithm recursively explores all possible paths from the root to the leaves. It checks if the current node is a leaf and if its value equals the remaining sum, adding the path to the result if true.

## Complexity
- Time: O(N^2) in the worst case, where N is the number of nodes in the tree, due to the copying of paths in the recursive calls.
- Space: O(N) for storing the recursive call stack and the space needed for the output.

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:
    vector<vector<int>> pathSum(TreeNode* root, int targetSum) {
        vector<vector<int>> result;
        vector<int> path;
        dfs(root, targetSum, path, result);
        return result;
    }
    
    void dfs(TreeNode* node, int remainingSum, vector<int>& path, vector<vector<int>>& result) {
        if (!node) return;
        
        path.push_back(node->val);
        remainingSum -= node->val;
        
        if (!node->left && !node->right && remainingSum == 0) {
            result.push_back(path);
        } else {
            dfs(node->left, remainingSum, path, result);
            dfs(node->right, remainingSum, path, result);
        }
        
        path.pop_back(); // backtrack
    }
};
```

## Test Cases
```
Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: [[5,4,11,2],[5,8,4,5]]
```

## Key Takeaways
- The use of DFS allows for efficient exploration of all paths in the binary tree.
- Keeping track of the current path and its sum enables the identification of paths that match the target sum.
- Backtracking is essential for exploring all possible paths without modifying the original tree structure.