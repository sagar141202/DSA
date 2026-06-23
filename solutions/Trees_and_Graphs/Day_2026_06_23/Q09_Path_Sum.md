# Path Sum

## Problem Statement
Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where each path's sum equals targetSum. A path is considered valid if there is a path from the root to a leaf node, and the sum of all node values in the path equals targetSum. The binary tree has the following properties: the number of nodes in the tree is in the range [1, 100], -1000 <= Node.val <= 1000, and -10^3 <= targetSum <= 10^3.

## Approach
The approach to solve this problem is to use a depth-first search (DFS) algorithm to traverse the binary tree and keep track of the current path sum. If the current node is a leaf node and the path sum equals the target sum, add the path to the result list. The DFS function will recursively call itself for the left and right child nodes, updating the path sum and path list accordingly.

## Complexity
- Time: O(N^2) in the worst case, where N is the number of nodes in the tree, because we might need to traverse each node and for each node, we might need to create a copy of the current path.
- Space: O(N) for the recursion stack and O(N) for storing the paths, so the total space complexity is O(N).

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
Output: [[5,4,11,2],[5,8,4,5]]
```

## Key Takeaways
- Use DFS to solve problems that involve traversing a tree or graph and keeping track of the current path.
- Keep track of the current path sum and update it accordingly during the DFS traversal.
- Use a helper function to perform the DFS traversal and update the result list.