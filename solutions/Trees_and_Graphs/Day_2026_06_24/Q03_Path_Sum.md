# Path Sum

## Problem Statement
Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values equals the targetSum. The path must start at the root and end at a leaf node, and all node values in the path are added to the sum. The binary tree has the following structure: each node has a value, and two children (left and right). The problem constraints are: the number of nodes in the tree is in the range [0, 2000], -1000 <= Node.val <= 1000, and -10^3 <= targetSum <= 10^3.

## Approach
The approach to solve this problem is to use a depth-first search (DFS) algorithm to traverse the binary tree and calculate the sum of each path. We will use recursion to explore all possible paths and backtracking to remove the last added node when a dead end is reached. The algorithm will explore all root-to-leaf paths and check if the sum of each path equals the targetSum.

## Complexity
- Time: O(N^2) where N is the number of nodes in the binary tree, in the worst case when the tree is skewed to one side and we have to copy the path for each node.
- Space: O(N) where N is the number of nodes in the binary tree, for the recursion stack and the space needed to store the current path.

## C++ Solution
```cpp
#include <vector>
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
- Use DFS to traverse the binary tree and calculate the sum of each path.
- Use recursion to explore all possible paths and backtracking to remove the last added node when a dead end is reached.
- The time complexity is O(N^2) where N is the number of nodes in the binary tree, and the space complexity is O(N) for the recursion stack and the space needed to store the current path.