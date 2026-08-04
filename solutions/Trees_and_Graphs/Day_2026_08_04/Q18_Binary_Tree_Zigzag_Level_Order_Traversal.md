# Binary Tree Zigzag Level Order Traversal

## Problem Statement
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. The solution should handle trees of any size and shape, with node values being integers. For example, given a binary tree with the following structure:
```
    3
   / \
  9  20
    /  \
   15   7
```
The zigzag level order traversal would be `[[3], [20, 9], [15, 7]]`. The constraints are that the number of nodes in the tree will not exceed 2000, and the values of the nodes will be between -1000 and 1000.

## Approach
The solution uses a level order traversal (BFS) approach with a queue to traverse the tree level by level. It keeps track of the current level and whether to traverse from left to right or right to left. The algorithm uses a deque to store the nodes at each level.

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
            deque<int> level;
            
            for (int i = 0; i < size; i++) {
                TreeNode* node = q.front();
                q.pop();
                
                if (leftToRight) {
                    level.push_back(node->val);
                } else {
                    level.push_front(node->val);
                }
                
                if (node->left) q.push(node->left);
                if (node->right) q.push(node->right);
            }
            
            result.push_back(vector<int>(level.begin(), level.end()));
            leftToRight = !leftToRight;
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
Output: [[3], [20, 9], [15, 7]]

Input: 
    1
   / \
  2   3
 / \
4   5
Output: [[1], [3, 2], [4, 5]]
```

## Key Takeaways
- Use a queue for level order traversal (BFS) of the binary tree.
- Keep track of the current level and the direction of traversal (left to right or right to left).
- Utilize a deque to efficiently store and retrieve nodes at each level.