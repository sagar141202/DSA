# Binary Tree Level Order Traversal

## Problem Statement
Given the root of a binary tree, return the level order traversal of its nodes' values. The level order traversal of a binary tree is the traversal of the tree where we visit all the nodes at each level from left to right. For example, given the binary tree `[3,9,20,null,null,15,7]`, the level order traversal is `[[3],[9,20],[15,7]]`. The binary tree node is defined as `struct TreeNode { int val; TreeNode *left; TreeNode *right; TreeNode(int x) : val(x), left(NULL), right(NULL) {} };`. The input tree is guaranteed to have at most 2000 nodes, and the value of each node is in the range of `[0, 100]`.

## Approach
We use a queue-based approach to perform the level order traversal. We start by pushing the root node into the queue, and then we enter a loop where we keep removing nodes from the queue, adding their children to the queue, and adding the node's value to the current level's result.

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
        // Initialize the result vector and the queue
        vector<vector<int>> result;
        if (!root) return result;
        queue<TreeNode*> q;
        q.push(root);
        
        // Perform the level order traversal
        while (!q.empty()) {
            // Get the size of the current level
            int size = q.size();
            vector<int> level;
            
            // Process all nodes at the current level
            for (int i = 0; i < size; i++) {
                TreeNode* node = q.front();
                q.pop();
                level.push_back(node->val);
                
                // Add the children of the current node to the queue
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
- We use a queue to keep track of the nodes at each level.
- We use a vector to store the result, where each inner vector represents a level in the tree.
- We process all nodes at each level before moving on to the next level.