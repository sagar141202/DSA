# Binary Tree Level Order Traversal

## Problem Statement
Given the root of a binary tree, return the level order traversal of its nodes' values. The level order traversal of a binary tree is a sequence of lists where each list represents the nodes at a given level, from left to right. For example, given the following binary tree: 
```
    3
   / \
  9  20
    /  \
   15   7
```
The level order traversal of the above binary tree is `[[3], [9, 20], [15, 7]]`. The constraints are: the number of nodes in the tree is in the range `[0, 2000]`, `-1000 <= Node.val <= 1000`, and the tree is a non-empty binary tree.

## Approach
The algorithm uses a breadth-first search (BFS) approach to traverse the binary tree level by level. It utilizes a queue data structure to keep track of the nodes at each level. The algorithm starts with the root node, explores all the nodes at the current level, and then moves on to the next level.

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
        // Initialize the result vector
        vector<vector<int>> result;
        
        // If the tree is empty, return an empty vector
        if (!root) {
            return result;
        }
        
        // Initialize a queue with the root node
        queue<TreeNode*> q;
        q.push(root);
        
        // Perform BFS
        while (!q.empty()) {
            // Get the size of the current level
            int levelSize = q.size();
            
            // Initialize a vector to store the nodes at the current level
            vector<int> level;
            
            // Process all nodes at the current level
            for (int i = 0; i < levelSize; i++) {
                // Dequeue a node
                TreeNode* node = q.front();
                q.pop();
                
                // Add the node's value to the level vector
                level.push_back(node->val);
                
                // Enqueue the node's children if they exist
                if (node->left) {
                    q.push(node->left);
                }
                if (node->right) {
                    q.push(node->right);
                }
            }
            
            // Add the level vector to the result
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
- Use a queue to perform BFS on the binary tree.
- Process all nodes at each level before moving on to the next level.
- Use a vector to store the nodes' values at each level.