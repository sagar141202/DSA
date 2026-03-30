# Right Side View of Binary Tree

## Problem Statement
Given the root of a binary tree, return the rightmost node value at each depth level, from top to bottom. The input tree is a binary tree where each node has a unique value and has at most two children (i.e., left child and right child). The number of nodes in the tree is in the range [0, 100]. The input tree is not guaranteed to be balanced, and the height of the tree is in the range [0, 100]. For example, given the binary tree `[1,2,3,null,5,null,4]`, the right side view is `[1,3,4]`.

## Approach
The algorithm uses a breadth-first search (BFS) approach to traverse the binary tree level by level. It keeps track of the last node at each level and adds its value to the result list. This approach ensures that we get the rightmost node at each depth level.

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
        
        // Base case: if tree is empty
        if (!root) return result;
        
        // Initialize queue with root node
        queue<TreeNode*> q;
        q.push(root);
        
        // Traverse tree level by level
        while (!q.empty()) {
            // Get size of current level
            int size = q.size();
            
            // Process each node at current level
            for (int i = 0; i < size; i++) {
                // Dequeue a node
                TreeNode* node = q.front();
                q.pop();
                
                // If it's the last node at current level, add its value to result
                if (i == size - 1) result.push_back(node->val);
                
                // Enqueue its children if they exist
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
```

## Key Takeaways
- Use BFS to traverse the binary tree level by level.
- Keep track of the last node at each level to get the rightmost node.
- Use a queue to store nodes at each level for efficient traversal.