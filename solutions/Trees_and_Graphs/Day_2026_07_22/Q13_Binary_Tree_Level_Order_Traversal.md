# Binary Tree Level Order Traversal

## Problem Statement
Given the root of a binary tree, return the level order traversal of its nodes' values. The level order traversal of a binary tree is a sequence of nodes visited level by level from left to right, and from top to bottom. For example, given the binary tree `[3,9,20,null,null,15,7]`, the level order traversal is `[[3],[9,20],[15,7]]`. The binary tree node is defined as `struct TreeNode { int val; TreeNode *left; TreeNode *right; TreeNode(int x) : val(x), left(NULL), right(NULL) {} };`. The input tree is guaranteed to have at most 2000 nodes, and the value of each node is guaranteed to be within the range of 0 to 999.

## Approach
We use a queue to store nodes at each level, and then process them level by level. The algorithm starts by adding the root node to the queue, then enters a loop where it dequeues all nodes at the current level, adds their values to the result, and enqueues their children.

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
        // Initialize result and queue
        vector<vector<int>> result;
        if (!root) return result;
        queue<TreeNode*> q;
        q.push(root);
        
        // Process nodes level by level
        while (!q.empty()) {
            vector<int> level;
            int size = q.size();
            for (int i = 0; i < size; i++) {
                // Dequeue a node, add its value to the current level, and enqueue its children
                TreeNode* node = q.front(); q.pop();
                level.push_back(node->val);
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
- Use a queue to store nodes at each level for efficient level order traversal.
- Process nodes level by level by dequeuing all nodes at the current level, adding their values to the result, and enqueuing their children.
- The time complexity is O(N), where N is the number of nodes in the tree, since we visit each node once.