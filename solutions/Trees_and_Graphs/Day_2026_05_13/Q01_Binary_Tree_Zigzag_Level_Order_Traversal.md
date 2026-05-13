# Binary Tree Zigzag Level Order Traversal

## Problem Statement
Given a binary tree, return the zigzag level order traversal of its nodes' values. The zigzag level order traversal is defined as the level order traversal where the nodes at each level are traversed in alternating order (from left to right, then right to left, then left to right, and so on). For example, given a binary tree: `[3,9,20,null,null,15,7]`, the zigzag level order traversal would be `[[3],[20,9],[15,7]]`. The input tree is guaranteed to have at most 2000 nodes, and the values of the nodes are in the range of `0` to `4999`.

## Approach
We can solve this problem by using a level order traversal (BFS) approach, where we traverse the tree level by level and store the nodes' values in a result list. We use a flag to track whether we should traverse the current level from left to right or right to left.

## Complexity
- Time: O(N)
- Space: O(N)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        vector<vector<int>> result;
        if (!root) return result;
        
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
- Use a level order traversal (BFS) approach to traverse the tree.
- Use a flag to track whether to traverse the current level from left to right or right to left.
- Use a queue to store the nodes at each level.