# Binary Tree Zigzag Level Order Traversal

## Problem Statement
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. The solution should handle trees with up to 100 nodes and node values ranging from 0 to 100. For example, given the binary tree `[3,9,20,null,null,15,7]`, the output should be `[[3],[9,20],[15,7]]`. The tree is defined as follows: the root node is `3`, its left child is `9`, its right child is `20`, the left child of `20` is `15`, and the right child of `20` is `7`.

## Approach
The algorithm uses a queue to perform level order traversal and a flag to track the direction of traversal. It iterates over each level, adding node values to the result in the correct order based on the flag. The flag is toggled after each level to alternate the direction of traversal.

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
        if (!root) return {};
        
        vector<vector<int>> result;
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
Output: [[3],[9,20],[15,7]]
Input: [1]
Output: [[1]]
Input: []
Output: []
```

## Key Takeaways
- Use a queue to efficiently traverse the tree level by level.
- Utilize a flag to alternate the direction of traversal for each level.
- Consider edge cases, such as an empty tree or a tree with a single node.