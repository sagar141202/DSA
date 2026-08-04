# Binary Tree Level Order Traversal

## Problem Statement
Given the root of a binary tree, return the level order traversal of its nodes' values. The level order traversal of a binary tree is a sequence of lists where each list represents the values of the nodes at each level, from left to right, and from top to bottom. For example, given the following binary tree: 
       3
      / \
     9  20
       / \
      15  7
The level order traversal of the above binary tree is: [[3], [9, 20], [15, 7]]. 

## Approach
The algorithm uses a queue to perform a level order traversal of the binary tree. It starts by adding the root node to the queue, then iteratively removes nodes from the queue, adds their values to the current level, and adds their children to the queue.

## Complexity
- Time: O(N)
- Space: O(N)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        // Initialize result and queue
        vector<vector<int>> result;
        if (!root) return result;
        queue<TreeNode*> q;
        q.push(root);

        // Perform level order traversal
        while (!q.empty()) {
            // Get the size of the current level
            int size = q.size();
            // Initialize a vector to store the values of the current level
            vector<int> level;
            for (int i = 0; i < size; i++) {
                // Dequeue a node and add its value to the current level
                TreeNode* node = q.front();
                q.pop();
                level.push_back(node->val);
                // Enqueue the children of the current node
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
Input: root = [3, 9, 20, null, null, 15, 7]
Output: [[3], [9, 20], [15, 7]]
Input: root = [1]
Output: [[1]]
Input: root = []
Output: []
```

## Key Takeaways
- Use a queue to perform a level order traversal of a binary tree.
- Keep track of the size of the current level to iterate over all nodes at the current level.
- Dequeue a node, add its value to the current level, and enqueue its children to move to the next level.