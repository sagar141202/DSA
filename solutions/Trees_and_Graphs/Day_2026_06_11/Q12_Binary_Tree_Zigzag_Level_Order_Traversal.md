# Binary Tree Zigzag Level Order Traversal

## Problem Statement
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. The solution should return a list of lists, where each sublist contains the node values at each level. The first level should be traversed from left to right, the second level from right to left, and so on. For example, given the binary tree `[3,9,20,null,null,15,7]`, the output should be `[[3],[20,9],[15,7]]`. The input tree is guaranteed to have at most 2000 nodes, and the values of the nodes are guaranteed to be in the range `[0, 1000]`.

## Approach
The algorithm uses a level order traversal approach with a queue to store the nodes at each level. It also uses a flag to track the direction of traversal at each level. The flag is toggled after each level to alternate the direction of traversal.

## Complexity
- Time: O(N), where N is the number of nodes in the tree
- Space: O(N), where N is the number of nodes in the tree

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
        bool reverse = false;
        
        while (!q.empty()) {
            int size = q.size();
            vector<int> level;
            
            for (int i = 0; i < size; i++) {
                TreeNode* node = q.front();
                q.pop();
                if (reverse) level.insert(level.begin(), node->val);
                else level.push_back(node->val);
                
                if (node->left) q.push(node->left);
                if (node->right) q.push(node->right);
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
Input: [1]
Output: [[1]]
Input: []
Output: []
```

## Key Takeaways
- Use a level order traversal approach with a queue to store the nodes at each level.
- Use a flag to track the direction of traversal at each level.
- Toggle the flag after each level to alternate the direction of traversal.