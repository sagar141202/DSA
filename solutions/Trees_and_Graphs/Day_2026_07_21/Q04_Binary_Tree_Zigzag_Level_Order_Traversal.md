# Binary Tree Zigzag Level Order Traversal

## Problem Statement
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. The zigzag level order traversal starts from the leftmost node at each level and moves toward the right for odd levels, then toward the left for even levels. For example, given the binary tree `[3,9,20,null,null,15,7]`, the zigzag level order traversal is `[[3],[20,9],[15,7]]`. The binary tree node has the following structure: a `val` field representing the node's value, and `left` and `right` fields representing references to the left and right child nodes, respectively.

## Approach
The algorithm uses a breadth-first search (BFS) approach with a queue to traverse the tree level by level. It maintains a flag to track whether the current level should be traversed from left to right or right to left.

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
        vector<vector<int>> result;
        if (!root) return result;
        
        queue<TreeNode*> q;
        q.push(root);
        bool isReverse = false;
        
        while (!q.empty()) {
            int size = q.size();
            vector<int> level;
            
            for (int i = 0; i < size; i++) {
                TreeNode* node = q.front();
                q.pop();
                
                if (isReverse) {
                    level.insert(level.begin(), node->val);
                } else {
                    level.push_back(node->val);
                }
                
                if (node->left) q.push(node->left);
                if (node->right) q.push(node->right);
            }
            
            result.push_back(level);
            isReverse = !isReverse;
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
- Use a queue to perform BFS traversal.
- Maintain a flag to track the traversal order of each level.
- Use the `insert` method to add elements at the beginning of the vector for reverse traversal.