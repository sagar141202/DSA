# Binary Tree Level Order Traversal

## Problem Statement
Given the root of a binary tree, return the level order traversal of its nodes' values. The level order traversal of a binary tree is the visitation of all nodes at each level from left to right, from top to bottom. For example, given the binary tree `[3,9,20,null,null,15,7]`, the level order traversal is `[[3],[9,20],[15,7]]`. The binary tree node has a value and two children: left and right. The root of the binary tree is given as the input, and the output should be a 2D vector where each sub-vector represents the nodes at a particular level.

## Approach
The algorithm uses a breadth-first search (BFS) approach to traverse the binary tree level by level. It utilizes a queue data structure to store the nodes at each level. The algorithm starts by pushing the root node into the queue and then enters a loop where it dequeues a node, processes it, and enqueues its children.

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
        // Base case: if the tree is empty, return an empty vector
        if (!root) return {};

        // Initialize the result vector and the queue with the root node
        vector<vector<int>> result;
        queue<TreeNode*> q;
        q.push(root);

        // Perform BFS
        while (!q.empty()) {
            // Get the number of nodes at the current level
            int levelSize = q.size();
            vector<int> levelValues;

            // Process each node at the current level
            for (int i = 0; i < levelSize; i++) {
                // Dequeue a node
                TreeNode* node = q.front();
                q.pop();

                // Add the node's value to the current level's values
                levelValues.push_back(node->val);

                // Enqueue the node's children
                if (node->left) q.push(node->left);
                if (node->right) q.push(node->right);
            }

            // Add the current level's values to the result
            result.push_back(levelValues);
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
- Use a queue data structure to perform BFS on the binary tree.
- Process each node at the current level and enqueue its children to move to the next level.
- Store the values of each level in a separate vector and add it to the result vector.