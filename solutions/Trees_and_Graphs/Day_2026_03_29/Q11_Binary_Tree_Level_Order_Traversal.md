# Binary Tree Level Order Traversal

## Problem Statement
Given the root of a binary tree, return the level order traversal of its nodes' values. The level order traversal of a binary tree is a sequence of nodes' values in which for each level, the nodes are visited from left to right, and for each subsequent level, the nodes are visited from left to right. The input binary tree can have up to 10^4 nodes, and each node has a unique value between 1 and 10^5. The tree height can be up to 10^3.

## Approach
The algorithm uses a queue data structure to perform a breadth-first search (BFS) traversal of the binary tree. This approach ensures that all nodes at each level are visited before moving on to the next level. The BFS traversal is implemented using a queue, where each node is added to the queue and then its children are added in the next iteration.

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
        // Initialize an empty vector to store the result
        vector<vector<int>> result;
        
        // If the tree is empty, return an empty vector
        if (!root) return result;
        
        // Initialize a queue with the root node
        queue<TreeNode*> q;
        q.push(root);
        
        // Perform BFS traversal
        while (!q.empty()) {
            // Get the size of the current level
            int size = q.size();
            
            // Initialize a vector to store the node values at the current level
            vector<int> level;
            
            // Visit each node at the current level
            for (int i = 0; i < size; i++) {
                // Dequeue a node from the queue
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
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Input: root = [1]
Output: [[1]]

Input: root = []
Output: []
```

## Key Takeaways
- Use a queue data structure to perform a BFS traversal of the binary tree.
- Keep track of the size of the current level to ensure that all nodes at each level are visited before moving on to the next level.
- Use a vector to store the node values at each level and add it to the result after visiting all nodes at that level.