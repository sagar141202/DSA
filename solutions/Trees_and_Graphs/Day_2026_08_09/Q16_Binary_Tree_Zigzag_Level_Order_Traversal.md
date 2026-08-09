# Binary Tree Zigzag Level Order Traversal

## Problem Statement
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. The zigzag level order traversal is defined as the level order traversal where the nodes at each level are traversed from left to right for odd levels and from right to left for even levels. For example, given the binary tree `[3,9,20,null,null,15,7]`, the zigzag level order traversal is `[[3],[20,9],[15,7]]`. The input binary tree is guaranteed to have at most 2000 nodes, and the value of each node is guaranteed to be in the range `[0, 100]`.

## Approach
We can solve this problem by using a level order traversal (BFS) and reversing the levels at even indices. We use a queue to store the nodes at each level and then process them. For even levels, we simply reverse the list of node values before adding it to the result.

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
        bool isEvenLevel = false;
        
        while (!q.empty()) {
            int levelSize = q.size();
            vector<int> level;
            
            for (int i = 0; i < levelSize; i++) {
                TreeNode* node = q.front();
                q.pop();
                level.push_back(node->val);
                
                if (node->left) q.push(node->left);
                if (node->right) q.push(node->right);
            }
            
            if (isEvenLevel) reverse(level.begin(), level.end());
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
- Use level order traversal (BFS) to process nodes level by level.
- Reverse the node values at even levels to achieve the zigzag effect.
- Utilize a queue to efficiently store and process nodes at each level.