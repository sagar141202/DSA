# Binary Tree Zigzag Level Order Traversal

## Problem Statement
Given a binary tree, return the zigzag level order traversal of its nodes' values. The traversal should start from the root, then move to the left subtree and the right subtree in a zigzag pattern. For example, given the binary tree `[3,9,20,null,null,15,7]`, the zigzag level order traversal is `[[3],[20,9],[15,7]]`. The input is the root of a binary tree, and the output is a 2D vector containing the nodes' values in the zigzag level order traversal. The constraints are that the number of nodes in the tree is in the range `[0, 2000]`, and the value of each node is in the range `[-100, 100]`.

## Approach
The algorithm uses a level order traversal (BFS) approach with a queue to traverse the tree level by level. It uses a flag to track the direction of traversal at each level. If the flag is true, it traverses the level from left to right; otherwise, it traverses from right to left.

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
        if (root == nullptr) return result;
        
        queue<TreeNode*> q;
        q.push(root);
        bool leftToRight = true;
        
        while (!q.empty()) {
            int size = q.size();
            vector<int> level;
            
            for (int i = 0; i < size; i++) {
                TreeNode* node = q.front();
                q.pop();
                
                if (leftToRight) {
                    level.push_back(node->val);
                } else {
                    level.insert(level.begin(), node->val);
                }
                
                if (node->left) q.push(node->left);
                if (node->right) q.push(node->right);
            }
            
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
- Use a queue to perform level order traversal of the binary tree.
- Use a flag to track the direction of traversal at each level.
- Use the `insert` method to add elements to the beginning of the level vector when traversing from right to left.