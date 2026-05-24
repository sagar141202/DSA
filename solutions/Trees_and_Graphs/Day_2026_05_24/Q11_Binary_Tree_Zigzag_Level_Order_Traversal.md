# Binary Tree Zigzag Level Order Traversal

## Problem Statement
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. The zigzag level order traversal is defined as follows: for each given tree level from left to right, if the level is odd, then the nodes' values should be listed from left to right; if the level is even, then the nodes' values should be listed from right to left. The root of the binary tree is given as `root = [3,9,20,null,null,15,7]`. The constraint is that the number of nodes in the tree is in the range `[0, 2000]`, and `-100 <= Node.val <= 100`.

## Approach
To solve this problem, we can use a level order traversal (BFS) approach and alternate the direction of traversal for each level. We will use a queue to store the nodes at each level and a flag to track the direction of traversal.

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
        if (!root) return {};
        
        vector<vector<int>> result;
        queue<TreeNode*> q;
        q.push(root);
        bool leftToRight = true;
        
        while (!q.empty()) {
            int levelSize = q.size();
            vector<int> level;
            
            for (int i = 0; i < levelSize; i++) {
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
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]
```

## Key Takeaways
- Use a level order traversal approach to solve the problem.
- Alternate the direction of traversal for each level using a flag.
- Use a queue to store the nodes at each level and process them accordingly.