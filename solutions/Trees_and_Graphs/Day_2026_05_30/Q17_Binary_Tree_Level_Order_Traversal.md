# Binary Tree Level Order Traversal

## Problem Statement
Given the root of a binary tree, return the level order traversal of its nodes' values. The level order traversal of a binary tree is a sequence of arrays where each array contains the node values at a given level, from left to right. For example, given the binary tree `[3,9,20,null,null,15,7]`, the level order traversal is `[[3],[9,20],[15,7]]`. The binary tree node is defined as `struct TreeNode { int val; TreeNode *left; TreeNode *right; TreeNode() : val(0), left(nullptr), right(nullptr) {}; TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}; TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}; };`. The input tree is guaranteed to have at most 2000 nodes and the value of each node is guaranteed to be in the range `[0, 100]`.

## Approach
The algorithm uses a queue data structure to perform a breadth-first search (BFS) traversal of the binary tree. It starts by enqueuing the root node, then iteratively dequeues a node, adds its children to the queue, and repeats the process until the queue is empty. This ensures that nodes are visited in level order.

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
        // Initialize result vector and queue
        vector<vector<int>> result;
        if (!root) return result;
        
        queue<TreeNode*> q;
        q.push(root);
        
        while (!q.empty()) {
            // Get the size of the current level
            int levelSize = q.size();
            vector<int> level;
            
            // Process each node in the current level
            for (int i = 0; i < levelSize; i++) {
                TreeNode* node = q.front();
                q.pop();
                level.push_back(node->val);
                
                // Add children to the queue for the next level
                if (node->left) q.push(node->left);
                if (node->right) q.push(node->right);
            }
            
            // Add the current level to the result
            result.push_back(level);
        }
        
        return result;
    }
};
```

## Test Cases
```
Input: 
    3
   / \
  9  20
    /  \
   15   7
Output: [[3],[9,20],[15,7]]

Input: 
    1
Output: [[1]]
```

## Key Takeaways
- Use a queue to perform a breadth-first search (BFS) traversal of the binary tree.
- Process each node in the current level before moving to the next level.
- Add children to the queue for the next level to ensure they are visited in the correct order.