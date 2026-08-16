# Path Sum

## Problem Statement
Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum. The path must start at the root and end at a leaf node, and all node values in the path must be summed to reach the targetSum. The binary tree node has a value, a left child node, and a right child node.

## Approach
The algorithm uses depth-first search to traverse the binary tree, maintaining a running sum of the node values in the current path. When a leaf node is reached, the algorithm checks if the running sum equals the targetSum. If it does, the current path is added to the result.

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

    void dfs(TreeNode* node, int remainingSum, vector<int>& path, vector<vector<int>>& result) {
        if (!node) return;
        path.push_back(node->val);
        if (!node->left && !node->right && node->val == remainingSum) {
            result.push_back(path);
        }
        dfs(node->left, remainingSum - node->val, path, result);
        dfs(node->right, remainingSum - node->val, path, result);
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
- Use depth-first search to efficiently traverse the binary tree.
- Maintain a running sum of the node values in the current path to avoid redundant calculations.
- Use a recursive approach to simplify the implementation and improve readability.