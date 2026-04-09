# Binary Tree Level Order Traversal

## Problem Statement
Given a binary tree, return the level order traversal of its nodes' values. The level order traversal of a binary tree is the traversal of the tree where we visit all nodes at a given depth level before moving on to the next depth level. The tree has the following constraints: the number of nodes in the tree is in the range [0, 2000], -1000 <= Node.val <= 1000, and the tree is a non-empty binary tree. For example, given a binary tree with the following structure: 
       3
      / \
     9  20
       /  \
      15   7
The level order traversal of this tree is [[3], [9, 20], [15, 7]].

## Approach
We can solve this problem by using a Breadth-First Search (BFS) algorithm. The algorithm starts at the root node, explores all the nodes at the present depth prior to moving on to the nodes at the next depth level. This process continues until all the nodes in the tree have been visited.

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
        
        // Continue the BFS traversal until the queue is empty
        while (!q.empty()) {
            // Get the size of the current level
            int levelSize = q.size();
            // Initialize a vector to store the node values at the current level
            vector<int> level;
            
            // Visit all the nodes at the current level
            for (int i = 0; i < levelSize; i++) {
                // Dequeue a node from the front of the queue
                TreeNode* node = q.front();
                q.pop();
                // Add the node's value to the level vector
                level.push_back(node->val);
                
                // Enqueue the node's children if they exist
                if (node->left) q.push(node->left);
                if (node->right) q.push(node->right);
            }
            // Add the level vector to the result vector
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
Output: [[3], [9, 20], [15, 7]]

Input: 
    1
Output: [[1]]

Input: 
Output: []
```

## Key Takeaways
- Use a BFS algorithm to traverse the tree level by level.
- Utilize a queue data structure to keep track of the nodes at each level.
- Keep track of the size of the current level to ensure that all nodes at the current level are visited before moving on to the next level.