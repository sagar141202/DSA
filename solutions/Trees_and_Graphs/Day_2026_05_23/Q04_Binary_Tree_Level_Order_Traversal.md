# Binary Tree Level Order Traversal

## Problem Statement
Given the root of a binary tree, return the level order traversal of its nodes' values. The level order traversal of a binary tree is a sequence of nodes' values in the order they appear when the tree is traversed level by level from left to right, and from top to bottom. For example, given a binary tree with the following structure: 
       3
      / \
     9  20
       /  \
      15   7
The level order traversal of the tree is: [[3], [9, 20], [15, 7]]. 

## Approach
The approach to solve this problem is to use a queue data structure to perform a breadth-first search (BFS) traversal of the binary tree. We start by adding the root node to the queue, then enter a loop where we process each node at the current level and add its children to the queue.

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
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> result;
        if (!root) return result;
        
        queue<TreeNode*> q;
        q.push(root);
        
        while (!q.empty()) {
            int size = q.size();
            vector<int> level;
            
            for (int i = 0; i < size; i++) {
                TreeNode* node = q.front();
                q.pop();
                level.push_back(node->val);
                
                if (node->left) q.push(node->left);
                if (node->right) q.push(node->right);
            }
            
            result.push_back(level);
        }
        
        return result;
    }
};
```

## Test Cases
```
Input: 
       3
      / \
     9  20
       /  \
      15   7
Output: [[3], [9, 20], [15, 7]]

Input: 
    1
   / \
  2   3
 / \
4   5
Output: [[1], [2, 3], [4, 5]]
```

## Key Takeaways
- Use a queue data structure to perform a breadth-first search (BFS) traversal of the binary tree.
- Process each node at the current level and add its children to the queue.
- The time complexity of this solution is O(N), where N is the number of nodes in the tree.