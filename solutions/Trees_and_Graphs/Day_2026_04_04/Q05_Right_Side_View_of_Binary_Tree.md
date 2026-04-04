# Right Side View of Binary Tree

## Problem Statement
Given the root of a binary tree, return the rightmost node value at each level. The rightmost node value at each level is the last node value when traversing the level from left to right. The input tree is a binary tree where each node has a unique value and has at most two children (i.e., left child and right child). The number of nodes in the tree is in the range [1, 100]. The values of the nodes in the tree are in the range [1, 100]. For example, given the binary tree `[1,2,3,null,5,null,4]`, the right side view is `[1,3,4]`.

## Approach
We can solve this problem by using a level order traversal (BFS) approach. We traverse each level of the tree from left to right and keep track of the last node value at each level. We use a queue to store the nodes at each level and update the result list with the last node value at each level.

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
        // Initialize result vector
        vector<int> result;
        
        // Base case: if the tree is empty
        if (!root) return result;
        
        // Initialize queue with the root node
        queue<TreeNode*> q;
        q.push(root);
        
        // Traverse the tree level by level
        while (!q.empty()) {
            // Get the number of nodes at the current level
            int levelSize = q.size();
            
            // Traverse the nodes at the current level
            for (int i = 0; i < levelSize; i++) {
                // Dequeue a node
                TreeNode* node = q.front();
                q.pop();
                
                // If this is the last node at the current level, add its value to the result
                if (i == levelSize - 1) {
                    result.push_back(node->val);
                }
                
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
Input: [1]
Output: [1]
Input: []
Output: []
```

## Key Takeaways
- Use level order traversal (BFS) to solve this problem.
- Keep track of the last node value at each level.
- Use a queue to store the nodes at each level.