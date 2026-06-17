# Right Side View of Binary Tree

## Problem Statement
Given the root of a binary tree, return the rightmost node value at each depth level. The rightmost node at each level is the last node when traversing the level from left to right. The input tree is a binary tree where each node has a value and at most two children (i.e., left child and right child). The number of nodes in the tree is in the range [0, 100]. The values of the nodes in the tree are in the range [-100, 100]. For example, given the binary tree `[1,2,3,null,5,null,4]`, the right side view is `[1,3,4]`.

## Approach
The approach to solve this problem is to use a level order traversal (BFS) of the binary tree, where we keep track of the last node at each level. We can use a queue to store the nodes at each level and then add the last node's value to the result.

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
    vector<int> rightSideView(TreeNode* root) {
        if (!root) return {};
        
        vector<int> result;
        queue<TreeNode*> q;
        q.push(root);
        
        while (!q.empty()) {
            int levelSize = q.size();
            for (int i = 0; i < levelSize; i++) {
                TreeNode* node = q.front();
                q.pop();
                
                if (i == levelSize - 1) {
                    result.push_back(node->val);
                }
                
                if (node->left) q.push(node->left);
                if (node->right) q.push(node->right);
            }
        }
        
        return result;
    }
};
```

## Test Cases
```
Input: [1,2,3,null,5,null,4]
Output: [1,3,4]
Input: [1,null,3]
Output: [1,3]
Input: []
Output: []
```

## Key Takeaways
- Use level order traversal (BFS) to solve the problem.
- Keep track of the last node at each level.
- Use a queue to store the nodes at each level.