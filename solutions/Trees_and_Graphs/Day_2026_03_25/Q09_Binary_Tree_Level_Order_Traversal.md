# Binary Tree Level Order Traversal

## Problem Statement
Given a binary tree, return the level order traversal of its nodes' values. The level order traversal of a binary tree is the traversal where we visit all the nodes at each level before moving on to the next level. For example, given a binary tree: `[3,9,20,null,null,15,7]`, the level order traversal is `[[3],[9,20],[15,7]]`. The binary tree node is defined as `struct TreeNode { int val; TreeNode *left; TreeNode *right; TreeNode(int x) : val(x), left(NULL), right(NULL) {} };`. The input is the root of the binary tree and the output is a vector of vectors where each inner vector represents the nodes at a particular level.

## Approach
The approach is to use a queue to keep track of the nodes at each level. We start by adding the root node to the queue, then we enter a loop where we keep removing nodes from the queue, add their children to the queue, and add their values to the result.

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
        // Initialize the result and the queue
        vector<vector<int>> result;
        if (!root) return result;
        queue<TreeNode*> q;
        q.push(root);
        
        // Traverse the tree level by level
        while (!q.empty()) {
            vector<int> level;
            int size = q.size();
            for (int i = 0; i < size; i++) {
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
- We use a queue to keep track of the nodes at each level.
- We use a vector of vectors to store the result, where each inner vector represents the nodes at a particular level.
- The time complexity is O(N) where N is the number of nodes in the tree, because we visit each node once.