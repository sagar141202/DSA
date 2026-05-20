# Binary Tree Zigzag Level Order Traversal

## Problem Statement
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. The zigzag level order traversal is defined as the level order traversal where the nodes at each level are traversed in an alternating manner (left to right, then right to left, then left to right, and so on). The input tree is a binary tree where each node has a value and two children (left and right). The number of nodes in the tree is between 1 and 200. The values of the nodes are between -100 and 100.

## Approach
The algorithm uses a level order traversal approach with a queue data structure to traverse the tree level by level. It keeps track of the current level and reverses the level order traversal when the level is odd. The algorithm uses a deque to efficiently reverse the level order traversal.

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
        bool reverse = false;
        
        while (!q.empty()) {
            int size = q.size();
            deque<int> level;
            
            for (int i = 0; i < size; i++) {
                TreeNode* node = q.front();
                q.pop();
                
                if (reverse) {
                    level.push_front(node->val);
                } else {
                    level.push_back(node->val);
                }
                
                if (node->left) q.push(node->left);
                if (node->right) q.push(node->right);
            }
            
            result.push_back(vector<int>(level.begin(), level.end()));
            reverse = !reverse;
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
- Use a queue to perform level order traversal of the tree.
- Use a deque to store the nodes at each level and reverse the deque when the level is odd.
- Keep track of the current level and reverse the level order traversal when the level is odd.