# Binary Tree Level Order Traversal

## Problem Statement
Given a binary tree, return the level order traversal of its nodes' values. The level order traversal of a binary tree is the traversal of the tree where we visit all the nodes at each level before moving on to the next level. For example, given the binary tree `[3,9,20,null,null,15,7]`, the level order traversal is `[[3],[9,20],[15,7]]`. The binary tree node has the following definition: `struct TreeNode { int val; TreeNode *left; TreeNode *right; TreeNode() : val(0), left(nullptr), right(nullptr) {}; TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}; TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}; }`. The input is the root of the binary tree and the output is a 2D vector containing the level order traversal of the binary tree.

## Approach
We can use a Breadth-First Search (BFS) algorithm to traverse the binary tree level by level. We will use a queue to store the nodes at each level. We will start by adding the root node to the queue, then we will enter a loop where we will keep removing nodes from the queue, add their values to the result, and add their children to the queue until the queue is empty.

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
        // Initialize the result and the queue
        vector<vector<int>> result;
        if (root == nullptr) {
            return result;
        }
        queue<TreeNode*> q;
        q.push(root);

        // Perform BFS
        while (!q.empty()) {
            // Get the size of the current level
            int size = q.size();
            vector<int> level;

            // Process all nodes at the current level
            for (int i = 0; i < size; i++) {
                TreeNode* node = q.front();
                q.pop();
                level.push_back(node->val);

                // Add children to the queue
                if (node->left != nullptr) {
                    q.push(node->left);
                }
                if (node->right != nullptr) {
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
- Use BFS to traverse the binary tree level by level.
- Use a queue to store the nodes at each level.
- Process all nodes at the current level before moving on to the next level.