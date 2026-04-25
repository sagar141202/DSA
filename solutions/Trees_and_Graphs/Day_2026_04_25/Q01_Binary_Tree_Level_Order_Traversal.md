# Binary Tree Level Order Traversal

## Problem Statement
Given a binary tree, return the level order traversal of its nodes' values. The level order traversal of a binary tree is the traversal of the tree from left to right, level by level, where the nodes at each level are visited in order from left to right. For example, given the binary tree `[3,9,20,null,null,15,7]`, the level order traversal is `[[3],[9,20],[15,7]]`. The binary tree node is defined as `struct TreeNode { int val; TreeNode *left; TreeNode *right; TreeNode(int x) : val(x), left(NULL), right(NULL) {} };`. The input tree is guaranteed to have at most 100 nodes, and the values of the nodes are in the range of 0 to 100.

## Approach
The approach is to use a queue data structure to perform a breadth-first search (BFS) traversal of the binary tree. At each level, we add the node values to the result list and then add their children to the queue for the next level. This ensures that we visit the nodes level by level from left to right.

## Complexity
- Time: O(N)
- Space: O(N)

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
    vector<vector<int>> levelOrder(TreeNode* root) {
        // Base case: if the tree is empty, return an empty list
        if (!root) {
            return {};
        }
        
        // Initialize the result list and the queue with the root node
        vector<vector<int>> result;
        queue<TreeNode*> q;
        q.push(root);
        
        // Perform BFS traversal
        while (!q.empty()) {
            int size = q.size();
            vector<int> level;
            
            // Process all nodes at the current level
            for (int i = 0; i < size; i++) {
                TreeNode* node = q.front();
                q.pop();
                level.push_back(node->val);
                
                // Add children to the queue for the next level
                if (node->left) {
                    q.push(node->left);
                }
                if (node->right) {
                    q.push(node->right);
                }
            }
            
            // Add the current level to the result list
            result.push_back(level);
        }
        
        return result;
    }
};
```

## Test Cases
```
Input: [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
Input: [1]
Output: [[1]]
Input: []
Output: []
```

## Key Takeaways
- Use a queue to perform BFS traversal of the binary tree.
- At each level, process all nodes and add their children to the queue for the next level.
- The time complexity is O(N), where N is the number of nodes in the tree, since we visit each node exactly once.