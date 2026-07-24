# Path Sum

## Problem Statement
Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values equals the targetSum. A root-to-leaf path is a path from the root to any leaf node in the tree. The path must contain at least one node and all nodes on the path must be connected by an edge. The tree has the following properties: the number of nodes in the tree is in the range [1, 100], -1000 <= Node.val <= 1000, and -1000 <= targetSum <= 1000.

## Approach
The algorithm uses a depth-first search (DFS) approach to traverse the binary tree, keeping track of the current path sum and storing the paths that sum up to the target. The DFS function is recursive, exploring the left and right subtrees and backtracking when necessary.

## Complexity
- Time: O(N^2) in the worst case, where N is the number of nodes in the tree, due to the path construction and copying.
- Space: O(N) for the recursion stack and path storage.

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
- Use DFS to efficiently explore the tree and keep track of the current path sum.
- Backtrack by removing the last node from the path when exploring other branches.
- Store the paths that sum up to the targetSum in the result vector.