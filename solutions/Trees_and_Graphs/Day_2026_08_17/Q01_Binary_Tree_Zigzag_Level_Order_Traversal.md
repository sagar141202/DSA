# Binary Tree Zigzag Level Order Traversal

## Problem Statement
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. The zigzag level order traversal is defined as the level order traversal of the binary tree, but with each level's nodes listed in alternating order (from left to right, then right to left, and so on). For example, given the binary tree `[3,9,20,null,null,15,7]`, the zigzag level order traversal is `[[3],[9,20],[15,7]]`. The input binary tree is guaranteed to have at most 2000 nodes, and the value of each node is guaranteed to be within the range `[0, 100000]`.

## Approach
We will use a level order traversal (BFS) approach to solve this problem. We will use a queue to keep track of the nodes at each level and a flag to determine the order of traversal at each level. The flag will be toggled at each level to achieve the zigzag effect.

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
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        // Initialize the result vector and the queue
        vector<vector<int>> result;
        if (root == nullptr) return result;
        queue<TreeNode*> q;
        q.push(root);
        bool leftToRight = true;

        // Perform level order traversal
        while (!q.empty()) {
            int size = q.size();
            vector<int> level;

            // Traverse each node at the current level
            for (int i = 0; i < size; i++) {
                TreeNode* node = q.front();
                q.pop();

                // Add the node's value to the level vector
                if (leftToRight) {
                    level.push_back(node->val);
                } else {
                    level.insert(level.begin(), node->val);
                }

                // Add the node's children to the queue
                if (node->left != nullptr) q.push(node->left);
                if (node->right != nullptr) q.push(node->right);
            }

            // Add the level vector to the result and toggle the direction
            result.push_back(level);
            leftToRight = !leftToRight;
        }

        return result;
    }
};
```

## Test Cases
```
Input: [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]
Input: [1]
Output: [[1]]
Input: []
Output: []
```

## Key Takeaways
- Use a level order traversal (BFS) approach to solve this problem.
- Use a flag to determine the order of traversal at each level and toggle it at each level to achieve the zigzag effect.
- Use a queue to keep track of the nodes at each level.