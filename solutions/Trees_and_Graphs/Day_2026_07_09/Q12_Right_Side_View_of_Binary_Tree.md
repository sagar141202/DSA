# Right Side View of Binary Tree

## Problem Statement
Given the root of a binary tree, return the rightmost node value at each level. The rightmost node value at each level is the last node value when traversing the level from left to right. The input tree is a binary tree where each node has a unique value. The number of nodes in the tree is in the range [1, 100]. The input tree is not guaranteed to be balanced. For example, given the binary tree `[1,2,3,null,5,null,4]`, the right side view is `[1,3,4]`.

## Approach
The approach to solve this problem is to use a breadth-first search (BFS) algorithm to traverse the tree level by level. At each level, we will store the last node value, which will be the rightmost node value at that level. We will use a queue to store the nodes at each level.

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
        // If the tree is empty, return an empty vector
        if (!root) return {};
        
        // Initialize the result vector and the queue
        vector<int> result;
        queue<TreeNode*> q;
        q.push(root);
        
        // Traverse the tree level by level
        while (!q.empty()) {
            // Get the size of the current level
            int size = q.size();
            
            // Traverse the nodes at the current level
            for (int i = 0; i < size; i++) {
                // Dequeue a node
                TreeNode* node = q.front();
                q.pop();
                
                // If this is the last node at the current level, add its value to the result
                if (i == size - 1) result.push_back(node->val);
                
                // Enqueue the children of the current node
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
- Use BFS to traverse the tree level by level.
- At each level, store the last node value, which will be the rightmost node value at that level.
- Use a queue to store the nodes at each level.