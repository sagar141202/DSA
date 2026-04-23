# Binary Tree Level Order Traversal

## Problem Statement
Given the root of a binary tree, return the level order traversal of its nodes' values. The level order traversal of a binary tree is a sequence of lists where each list represents the nodes at a given level, from left to right, starting from the root. For example, given the binary tree `[3,9,20,null,null,15,7]`, the level order traversal is `[[3],[9,20],[15,7]]`. The input tree is guaranteed to have at most 2000 nodes, and the value of each node is guaranteed to be within the range `[0, 100]`.

## Approach
The algorithm uses a queue to perform a breadth-first search (BFS) traversal of the binary tree. It starts by adding the root node to the queue, then iteratively removes nodes from the front of the queue, adds their children to the back of the queue, and records the node values at each level.

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
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        // Initialize the result vector and the queue with the root node
        vector<vector<int>> result;
        if (!root) return result;
        queue<TreeNode*> q;
        q.push(root);
        
        // Perform BFS traversal
        while (!q.empty()) {
            // Get the number of nodes at the current level
            int levelSize = q.size();
            vector<int> levelNodes;
            
            // Process each node at the current level
            for (int i = 0; i < levelSize; i++) {
                TreeNode* node = q.front();
                q.pop();
                levelNodes.push_back(node->val);
                
                // Add child nodes to the queue for the next level
                if (node->left) q.push(node->left);
                if (node->right) q.push(node->right);
            }
            
            // Add the current level nodes to the result
            result.push_back(levelNodes);
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
- Process each node at the current level before moving to the next level.
- Record the node values at each level to construct the level order traversal result.