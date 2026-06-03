# Binary Tree Level Order Traversal

## Problem Statement
Given the root of a binary tree, return the level order traversal of its nodes' values. The traversal should be from left to right, and the levels should be represented in a list of lists, where the first list contains the nodes at level 1, the second list contains the nodes at level 2, and so on. For example, given the binary tree `[3,9,20,null,null,15,7]`, the level order traversal is `[[3],[9,20],[15,7]]`. The binary tree node has a value and two children, left and right.

## Approach
We can use a breadth-first search (BFS) algorithm to solve this problem, utilizing a queue to store the nodes at each level. We start by adding the root node to the queue, then iteratively dequeue a node, add its value to the current level's list, and enqueue its children.

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
        // If the tree is empty, return an empty list
        if (!root) return {};

        vector<vector<int>> result;
        queue<TreeNode*> q;
        q.push(root);

        // Continue until all levels have been processed
        while (!q.empty()) {
            int levelSize = q.size();
            vector<int> level;

            // Process all nodes at the current level
            for (int i = 0; i < levelSize; i++) {
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
Input: [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
Input: [1]
Output: [[1]]
Input: []
Output: []
```

## Key Takeaways
- Use BFS to traverse the tree level by level
- Utilize a queue to store the nodes at each level
- Process all nodes at the current level before moving to the next level