# Binary Tree Level Order Traversal

## Problem Statement
Given the root of a binary tree, return the level order traversal of its nodes' values. The level order traversal of a binary tree is a sequence of lists where each list represents the nodes at a given level, from left to right. For example, given the binary tree `[3,9,20,null,null,15,7]`, the level order traversal is `[[3],[9,20],[15,7]]`. The input tree is guaranteed to have at most 2000 nodes, and the values of the nodes are in the range `[0, 10000]`.

## Approach
The algorithm uses a queue to perform a breadth-first search (BFS) traversal of the binary tree. It starts by adding the root node to the queue, then enters a loop where it dequeues each node, adds its value to the current level's list, and enqueues its children. Once all nodes at the current level have been processed, the level's list is added to the result.

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
        vector<vector<int>> result;
        if (!root) return result;
        
        queue<TreeNode*> q;
        q.push(root);
        
        while (!q.empty()) {
            int levelSize = q.size();
            vector<int> level;
            
            for (int i = 0; i < levelSize; i++) {
                TreeNode* node = q.front();
                q.pop();
                level.push_back(node->val);
                
                if (node->left) q.push(node->left);
                if (node->right) q.push(node->right);
            }
            
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
- Use a queue to perform BFS traversal of the binary tree.
- Keep track of the current level's size to know when to move to the next level.
- Add each node's value to the current level's list and enqueue its children.