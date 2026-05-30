# Binary Tree Zigzag Level Order Traversal

## Problem Statement
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. The zigzag level order traversal starts from the leftmost node of the first level, then moves to the right, then moves to the left, and so on. For example, given the binary tree `[3,9,20,null,null,15,7]`, the zigzag level order traversal is `[[3],[9,20],[15,7]]`. The input tree is guaranteed to have at most 2000 nodes, and the value of each node is guaranteed to be within the range [-2^31, 2^31 - 1].

## Approach
We can solve this problem using a level order traversal (BFS) approach with a queue data structure. We will traverse the tree level by level, and for each level, we will check if it's an even or odd level to determine the order of traversal. If it's an even level, we will traverse from left to right, and if it's an odd level, we will traverse from right to left.

## Complexity
- Time: O(N)
- Space: O(N)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        vector<vector<int>> result;
        if (!root) return result;
        
        queue<TreeNode*> q;
        q.push(root);
        bool isEvenLevel = true;
        
        while (!q.empty()) {
            int size = q.size();
            vector<int> level;
            for (int i = 0; i < size; i++) {
                TreeNode* node = q.front();
                q.pop();
                
                if (isEvenLevel) {
                    level.push_back(node->val);
                } else {
                    level.insert(level.begin(), node->val);
                }
                
                if (node->left) q.push(node->left);
                if (node->right) q.push(node->right);
            }
            result.push_back(level);
            isEvenLevel = !isEvenLevel;
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
- Use a level order traversal (BFS) approach to solve the problem.
- Use a queue data structure to store the nodes at each level.
- Use a boolean variable to keep track of the current level (even or odd) and determine the order of traversal.