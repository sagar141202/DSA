# Binary Tree Zigzag Level Order Traversal

## Problem Statement
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. The solution should be able to handle trees with up to 10^4 nodes and node values ranging from 0 to 10^4. For example, given the binary tree `[3,9,20,null,null,15,7]`, the output should be `[[3],[9,20],[15,7]]`. The tree is defined as follows: the root node is `3`, its left child is `9`, its right child is `20`, the left child of `20` is `15`, and the right child of `20` is `7`.

## Approach
The algorithm uses a breadth-first search (BFS) approach, utilizing a queue to traverse the tree level by level. It keeps track of the current level and whether the nodes should be added in reverse order. The algorithm iterates over each level, adding the node values to the result list while maintaining the zigzag order.

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
        if (!root) {
            return result;
        }
        
        queue<TreeNode*> q;
        q.push(root);
        bool reverse = false;
        
        while (!q.empty()) {
            int size = q.size();
            vector<int> level;
            
            for (int i = 0; i < size; i++) {
                TreeNode* node = q.front();
                q.pop();
                
                if (reverse) {
                    level.insert(level.begin(), node->val);
                } else {
                    level.push_back(node->val);
                }
                
                if (node->left) {
                    q.push(node->left);
                }
                if (node->right) {
                    q.push(node->right);
                }
            }
            
            result.push_back(level);
            reverse = !reverse;
        }
        
        return result;
    }
};
```

## Test Cases
```
Input: [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]
```

## Key Takeaways
- Use BFS to traverse the tree level by level.
- Keep track of the current level and whether the nodes should be added in reverse order.
- Use a queue to store nodes to be processed and a vector to store the result.