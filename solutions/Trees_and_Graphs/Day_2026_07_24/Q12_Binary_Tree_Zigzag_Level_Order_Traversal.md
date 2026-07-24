# Binary Tree Zigzag Level Order Traversal

## Problem Statement
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. The traversal should start from the root, then alternate between left-to-right and right-to-left for each subsequent level. For example, given the binary tree `[3,9,20,null,null,15,7]`, the zigzag level order traversal is `[[3],[20,9],[15,7]]`. The input tree is guaranteed to have at most 2000 nodes, and the values of the nodes are in the range `[0, 100]`.

## Approach
We will use a level order traversal (BFS) approach with a queue to traverse the tree level by level. We will also maintain a flag to track the direction of traversal at each level.

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
- Use a queue to perform level order traversal of the binary tree.
- Maintain a flag to track the direction of traversal at each level.
- Use a vector to store the nodes at each level and insert/append nodes based on the current direction of traversal.