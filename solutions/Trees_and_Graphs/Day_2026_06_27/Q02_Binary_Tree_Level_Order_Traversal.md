# Binary Tree Level Order Traversal

## Problem Statement
Given a binary tree, return the level order traversal of its nodes' values. The level order traversal of a binary tree is the traversal of the tree where we visit all the nodes at each level before moving on to the next level. For example, given a binary tree: `[3,9,20,null,null,15,7]`, the level order traversal is: `[[3],[9,20],[15,7]]`. The binary tree node is defined as `struct TreeNode { int val; TreeNode *left; TreeNode *right; TreeNode(int x) : val(x), left(NULL), right(NULL) {} };`. The input is the root of the binary tree and the output is a 2D vector where each sub-vector represents the nodes at a particular level.

## Approach
We will use a breadth-first search (BFS) algorithm to traverse the binary tree level by level. We will use a queue to keep track of the nodes at each level. We will start by adding the root node to the queue, then we will enter a loop where we will keep removing nodes from the queue, add their children to the queue, and add their values to the result.

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
        // If the tree is empty, return an empty vector
        if (!root) {
            return {};
        }
        
        vector<vector<int>> result;
        queue<TreeNode*> q;
        q.push(root);
        
        // Continue the BFS traversal until the queue is empty
        while (!q.empty()) {
            int size = q.size();
            vector<int> level;
            
            // Process all nodes at the current level
            for (int i = 0; i < size; i++) {
                TreeNode* node = q.front();
                q.pop();
                level.push_back(node->val);
                
                // Add children of the current node to the queue
                if (node->left) {
                    q.push(node->left);
                }
                if (node->right) {
                    q.push(node->right);
                }
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
- Use a queue to perform BFS traversal of the binary tree.
- Keep track of the nodes at each level using a queue.
- Process all nodes at the current level before moving on to the next level.
- Add the values of the nodes at each level to the result.