# Path Sum

## Problem Statement
Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where each path's sum equals targetSum. A path is considered valid if there is a path from the root to a leaf node and the sum of all node values in the path equals the targetSum. The binary tree node has a value and two children (left and right). The function should return a 2D vector of vectors, where each inner vector represents a valid path.

## Approach
The algorithm uses a recursive depth-first search (DFS) approach to traverse the binary tree, keeping track of the current path and its sum. When a leaf node is reached, the algorithm checks if the current path sum equals the targetSum. If it does, the path is added to the result list.

## Complexity
- Time: O(N^2) in the worst case, where N is the number of nodes in the tree, due to the recursive DFS traversal and potential path copying.
- Space: O(N) for the recursive call stack and O(N) for storing the result paths, resulting in a total space complexity of O(N).

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
        vector<int> currentPath;
        dfs(root, targetSum, currentPath, result);
        return result;
    }
    
    void dfs(TreeNode* node, int remainingSum, vector<int>& currentPath, vector<vector<int>>& result) {
        if (node == nullptr) return;
        
        currentPath.push_back(node->val);
        remainingSum -= node->val;
        
        if (node->left == nullptr && node->right == nullptr && remainingSum == 0) {
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
- The problem can be solved using a recursive DFS approach with a time complexity of O(N^2) and space complexity of O(N).
- It's essential to keep track of the current path and its sum to efficiently find valid paths.
- The algorithm should handle edge cases, such as an empty tree or a tree with no valid paths.