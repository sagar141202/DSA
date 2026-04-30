# Binary Tree Zigzag Level Order Traversal

## Problem Statement
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. The zigzag level order traversal is defined as follows: for each given tree level from left to right, if the level is an odd number, the nodes are traversed from left to right, and if the level is an even number, the nodes are traversed from right to left. The root of the binary tree is given as input, and the function should return a 2D vector where each sub-vector represents a level in the binary tree. For example, given the binary tree [3,9,20,null,null,15,7], the function should return [[3],[20,9],[15,7]]. The binary tree node structure is defined as follows: each node has an integer value and two pointers, one pointing to the left child and one pointing to the right child.

## Approach
The algorithm uses a breadth-first search (BFS) approach to traverse the binary tree level by level. It utilizes a queue data structure to store the nodes at each level and a flag to track whether the current level should be traversed from left to right or right to left. The algorithm iterates through the queue, adding the node values to the result vector in the correct order based on the current level.

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
- The BFS approach is suitable for level order traversal problems.
- Using a queue data structure simplifies the process of traversing the tree level by level.
- A flag variable can be used to track the direction of traversal at each level.