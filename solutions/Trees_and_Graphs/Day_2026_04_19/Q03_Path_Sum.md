# Path Sum

## Problem Statement
Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values equals the targetSum. The path must start at the root and end at a leaf node, and each node's value is added to the sum. Examples include a tree with nodes having values 5, 4, 8, 11, 13, 4, 7, 2, where the target sum is 22. The output should be all paths where the sum equals the target sum, such as [[5,4,11,2], [5,8,4,5]].

## Approach
The algorithm uses a depth-first search (DFS) approach to traverse the binary tree, maintaining a running sum of node values from the root to the current node. If the current node is a leaf node and the running sum equals the target sum, the path is added to the result.

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
        
        // add current node to path
        path.push_back(node->val);
        targetSum -= node->val;
        
        // if current node is a leaf and sum equals target, add to result
        if (!node->left && !node->right && targetSum == 0) {
            result.push_back(path);
        } else {
            // recursively explore left and right subtrees
            dfs(node->left, targetSum, path, result);
            dfs(node->right, targetSum, path, result);
        }
        
        // remove current node from path (backtracking)
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
- Use DFS to traverse the binary tree, maintaining a running sum of node values.
- Backtrack by removing the current node from the path after exploring its subtrees.
- Add paths to the result when the current node is a leaf and the running sum equals the target sum.