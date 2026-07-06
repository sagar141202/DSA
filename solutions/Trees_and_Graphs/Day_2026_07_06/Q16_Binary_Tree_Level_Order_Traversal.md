# Binary Tree Level Order Traversal

## Problem Statement
Given the root of a binary tree, return the level order traversal of its nodes' values. The level order traversal of a binary tree is a sequence of arrays where each array represents the values of the nodes at a given level, from left to right. For example, given the binary tree `[3,9,20,null,null,15,7]`, the level order traversal is `[[3],[9,20],[15,7]]`. The binary tree node is defined as `struct TreeNode { int val; TreeNode *left; TreeNode *right; TreeNode() : val(0), left(nullptr), right(nullptr) {}; TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}; TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}; };`. The input is the root of the binary tree and the output is a vector of vectors, where each inner vector represents a level in the tree.

## Approach
The approach to solve this problem is to use a Breadth-First Search (BFS) algorithm, which traverses the tree level by level. We use a queue to store the nodes at each level and then process them. This way, we can easily get the level order traversal of the binary tree. The algorithm starts by pushing the root node into the queue, then enters a loop where it processes all nodes at the current level, and finally moves on to the next level.

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
        // If the tree is empty, return an empty vector
        if (!root) return {};
        
        // Initialize the result vector and the queue with the root node
        vector<vector<int>> result;
        queue<TreeNode*> q;
        q.push(root);
        
        // Continue the process until the queue is empty
        while (!q.empty()) {
            // Get the size of the current level
            int size = q.size();
            // Initialize a vector to store the values of the current level
            vector<int> level;
            
            // Process all nodes at the current level
            for (int i = 0; i < size; i++) {
                // Dequeue a node
                TreeNode* node = q.front();
                q.pop();
                // Add the node's value to the current level
                level.push_back(node->val);
                // Enqueue the node's children if they exist
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
Input: [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
Input: [1]
Output: [[1]]
Input: []
Output: []
```

## Key Takeaways
- We use a queue to store the nodes at each level and process them using BFS.
- The time complexity is O(N), where N is the number of nodes in the tree, because we visit each node once.
- The space complexity is O(N), where N is the number of nodes in the tree, because in the worst case, the queue will store all nodes at the last level.