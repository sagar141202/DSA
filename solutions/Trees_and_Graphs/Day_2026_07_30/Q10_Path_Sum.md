# Path Sum

## Problem Statement
Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where each path's sum equals targetSum. A path is considered valid if there is a path from the root to a leaf node and the sum of all node values in that path equals the targetSum. The binary tree node has a value and two children (left and right). The constraints are: the number of nodes in the tree is in the range [1, 100], -100 <= Node.val <= 100, and -1000 <= targetSum <= 1000.

## Approach
The approach to this problem involves using a depth-first search (DFS) algorithm to traverse the binary tree and calculate the sum of each path from the root to a leaf node. We will utilize recursion to explore all possible paths and keep track of the current path sum. If the current node is a leaf node and the path sum equals the target sum, we add the path to the result list.

## Complexity
- Time: O(N^2) in the worst case when the tree is skewed, where N is the number of nodes in the tree, because in the worst case, we might have to explore all nodes for each path.
- Space: O(N) for storing the current path and O(N) for the recursion stack in the worst case, so the total space complexity is O(N).

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
        
        // Add the current node's value to the path and update the remaining sum
        currentPath.push_back(node->val);
        remainingSum -= node->val;

        // If the current node is a leaf node and the remaining sum is zero, add the path to the result
        if (!node->left && !node->right && remainingSum == 0) {
            result.push_back(currentPath);
        }

        // Recursively explore the left and right subtrees
        dfs(node->left, remainingSum, currentPath, result);
        dfs(node->right, remainingSum, currentPath, result);

        // Remove the current node from the path to backtrack
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
- Use DFS to effectively explore all paths in the binary tree and calculate their sums.
- Utilize recursion to simplify the exploration of the tree and keep track of the current path sum.
- Backtrack by removing the current node from the path after exploring its subtrees to avoid unnecessary computations.