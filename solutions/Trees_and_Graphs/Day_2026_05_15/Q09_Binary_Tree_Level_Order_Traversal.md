# Binary Tree Level Order Traversal

## Problem Statement
Given the root of a binary tree, return the level order traversal of its nodes' values. The level order traversal of a binary tree is the traversal of the tree where nodes at each level are visited from left to right, top to bottom. For example, given a binary tree with the following structure:
```
    3
   / \
  9  20
    /  \
   15   7
```
The level order traversal would return `[[3], [9, 20], [15, 7]]`. The input binary tree is guaranteed to have at most 2000 nodes, and the value of each node is guaranteed to be within the range [-10^4, 10^4].

## Approach
The algorithm uses a breadth-first search (BFS) approach to traverse the binary tree level by level. It utilizes a queue data structure to store nodes at each level. The BFS traversal ensures that all nodes at a given level are visited before moving on to the next level.

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
        // Check if the input tree is empty
        if (!root) return {};
        
        // Initialize the result vector and the queue with the root node
        vector<vector<int>> result;
        queue<TreeNode*> q;
        q.push(root);
        
        // Perform BFS traversal
        while (!q.empty()) {
            // Get the number of nodes at the current level
            int levelSize = q.size();
            vector<int> levelValues;
            
            // Process each node at the current level
            for (int i = 0; i < levelSize; i++) {
                TreeNode* currentNode = q.front();
                q.pop();
                levelValues.push_back(currentNode->val);
                
                // Add child nodes to the queue for the next level
                if (currentNode->left) q.push(currentNode->left);
                if (currentNode->right) q.push(currentNode->right);
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
    1
   /
  2
 /
3
Output: [[1], [2], [3]]
```

## Key Takeaways
- Use a queue data structure to store nodes at each level for BFS traversal.
- Keep track of the number of nodes at each level to process them correctly.
- Add child nodes to the queue for the next level after processing the current node.